import requests
import time
import sys

# --- CONFIGURAZIONE ---
API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_API_SECRET(ONLY IF USE LIVESCORE)"
TELEGRAM_TOKEN = "YOUR_TG_TOKE"
CHAT_ID = "YOUR_CHAT_ID"

BASE_URL = "https://livescore-api.com/api-client"

# Memoria per i match: { match_id: num_reds }
tracked_matches = {}

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    bet_link = "https://www.bet365.it/#/IP/B1"
    payload = {
        "chat_id": CHAT_ID,
        "text": msg,
        "parse_mode": "Markdown",
        "reply_markup": {
            "inline_keyboard": [[{"text": "📱 Apri Bet365 Live", "url": bet_link}]]
        }
    }
    try:
        requests.post(url, json=payload, timeout=10)
    except Exception as e:
        print(f"❌ Errore invio Telegram: {e}")

def monitor_livescore():
    raw_matches = []
    # CICLO PAGINAZIONE: Scarichiamo fino a 5 pagine (500 match) per superare il limite di 100
    for p in range(1, 6):
        try:
            r = requests.get(f"{BASE_URL}/scores/live.json", 
                             params={"key": API_KEY, "secret": API_SECRET, "page": p},
                             timeout=15)
            data = r.json()
            if data.get('success'):
                page_data = data['data']['match']
                if not page_data: break # Se la pagina è vuota, stop
                raw_matches.extend(page_data)
                if len(page_data) < 100: break # Se sono meno di 100, non ci sono altre pagine
            else: break
        except Exception as e:
            print(f"⚠️ Errore API Pagina {p}: {e}")
            break

    # Rimuoviamo duplicati basandoci sull'ID del match
    unique_matches = {m['id']: m for m in raw_matches}.values()
    print(f"--- [{time.strftime('%H:%M:%S')}] Scansione Totale: {len(unique_matches)} match ---")

    for m in unique_matches:
        m_id = m['id']
        current_score = m['score']
        current_time = str(m['time'])
        country = m.get('location', 'Mondo')
        league = m.get('league_name', 'Campionato')

        # 1. RECUPERO EVENTI PER ROSSI
        events = []
        try:
            ev_r = requests.get(f"{BASE_URL}/scores/events.json", 
                                params={"key": API_KEY, "secret": API_SECRET, "id": m_id},
                                timeout=10)
            ev_res = ev_r.json()
            if ev_res.get('success'):
                events = ev_res['data']['event']
        except: pass

        red_cards_now = [e for e in events if e['event'] == 'RED_CARD']
        num_reds = len(red_cards_now)

        # 2. CONTROLLO NUOVI ROSSI SU MATCH GIÀ SEGNALATI
        if m_id in tracked_matches:
            prev_reds = tracked_matches[m_id]
            if num_reds > prev_reds:
                msg = (f"🟥 *ALTRO ROSSO RILEVATO!*\n"
                       f"🏆 {country} - {league}\n"
                       f"⚽ {m['home_name']} {current_score} {m['away_name']}\n"
                       f"⚠️ Situazione: {num_reds} espulsi totali!\n"
                       f"⏰ Minuto: {current_time}")
                send_telegram(msg)
                tracked_matches[m_id] = num_reds

            if current_time in ['FT', 'Finished', 'CANC']:
                del tracked_matches[m_id]
            continue

        # 3. FILTRI TEMPORALI (Sotto l'80°)
        if current_time in ['FT', 'Finished', 'POSTP', 'CANC', 'HT']: continue
        try:
            # Estraiamo il minuto pulito (gestisce 90+2)
            clean_time = "".join(filter(str.isdigit, current_time.split('+')[0]))
            if clean_time and int(clean_time) >= 80: continue
        except: pass

        # 4. LOGICA PRIMO ROSSO
        if num_reds > 0:
            red_event = red_cards_now[-1]
            score_parts = current_score.split(' - ')
            if len(score_parts) < 2: continue
            gh, ga = int(score_parts[0]), int(score_parts[1])
            diff_gol = abs(gh - ga)

            side = str(red_event.get('side', '')).lower()
            is_home_red = (side == 'home')
            is_away_red = (side == 'away')

            # Fallback se side non è presente
            if not is_home_red and not is_away_red:
                team_ev = str(red_event.get('team', '')).lower()
                if team_ev in m['home_name'].lower(): is_home_red = True
                elif team_ev in m['away_name'].lower(): is_away_red = True

            # CASO A: IDENTIFICATO E DI VALORE
            if (gh == ga) or (is_home_red and gh > ga) or (is_away_red and ga > gh):
                msg = (f"🚨 *VANTAGGIO STATISTICO*\n"
                       f"🌍 {country} - {league}\n"
                       f"⚽ {m['home_name']} {current_score} {m['away_name']}\n"
                       f"🟥 ROSSO: *{'CASA' if is_home_red else 'OSPITE'}*\n"
                       f"⏰ Minuto: {current_time}\n"
                       f"💡 Strategia: Forza 11 vs 10!")
                send_telegram(msg)
                tracked_matches[m_id] = num_reds

            # CASO B: INCERTO (Sconosciuto ma punteggio stretto)
            elif not is_home_red and not is_away_red:
                if gh == ga or diff_gol == 1:
                    msg = (f"❓ *MATCH INCERTO*\n"
                           f"🌍 {country} - {league}\n"
                           f"⚽ {m['home_name']} {current_score} {m['away_name']}\n"
                           f"🟥 Rosso rilevato (Incerto)\n"
                           f"⏰ Minuto: {current_time}\n"
                           f"⚠️ Verifica chi ha il rosso!")
                    send_telegram(msg)
                    tracked_matches[m_id] = num_reds

# --- AVVIO ---
if __name__ == "__main__":
    send_telegram("🚀 *BOT ATTIVATO* - Sblocco 100+ match attivo.")
    try:
        while True:
            monitor_livescore()
            time.sleep(300) # Scansione ogni 5 minuti
    except KeyboardInterrupt:
        send_telegram("🛑 *BOT DISATTIVATO*")
        sys.exit()