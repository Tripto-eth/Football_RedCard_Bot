


# ⚽ Football In-Play Red Card Alert Bot

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![API](https://img.shields.io/badge/API-Football%20v3-green?style=flat)
![Platform](https://img.shields.io/badge/Telegram-Bot-blue?style=flat&logo=telegram)

> **An automated Telegram bot designed to detect high-value betting opportunities by monitoring red cards and live match statistics.**

---

## 📖 Overview
This bot continuously scans live football data across major world leagues to identify specific match dynamics where a favorite remains dominant despite an opponent's red card. 

### Trigger Conditions:
* **🟥 Red Card Event:** Only triggers when a player is sent off.
* **📉 Ranking Gap:** Only alerts if the team with the red card is ranked **lower** in the standings than their opponent (Underdog).
* **⏱️ Time Remaining:** Only triggers if there are at least **20 minutes** of play remaining (Minute < 70').
* **📊 Dominance Metrics:** Automatically pulls possession percentage and shot counts to confirm the favorite's dominance.

---

## 🚀 Key Features
* **Real-time Monitoring:** Scans live matches every 5 minutes.
* **Smart Standings Integration:** Automatically downloads league tables to determine the "underdog" vs the "favorite."
* **Telegram Notifications:** Instant alerts delivered directly to your phone with Markdown formatting.
* **Wide League Coverage:** Pre-configured for Serie A, Premier League, La Liga, Bundesliga, Ligue 1, and more.

---

## 📊 Sample Alert
When a match meets the criteria, you receive a message like this:

```text
🟥 RED CARD ALERT: UNDERDOG DISADVANTAGE

🏟 Team A (Home) vs Team B (Away)
⏱ Minute: 62'

📊 LIVE STATISTICS (H/A):
📈 Possession: 65% - 35%
⚽ Total Shots: 12 - 3

🏆 LEAGUE RANK:
🏠 Team A: 3rd
🚀 Team B: 18th (RED CARD)

⚠️ Note: The lower-ranked team is down to 10 men.

```

---

## 🛠 Tech Stack

The bot is built using a lightweight and efficient stack:

* **Language:** Python 3.x
* **Data Source:** [API-Football](https://www.api-football.com/) (V3) via RapidAPI
* **Messaging:** Telegram Bot API
* **Networking:** `requests` library

---

## ⚙️ Setup & Installation

Follow these steps to get your bot up and running:

### 1. Clone the Repository

> ⚠️ **IMPORTANT:** Keep this repository **PRIVATE** to protect your API keys and Telegram credentials.

```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
cd YOUR_REPO_NAME

```

### 2. Install Dependencies

Make sure you have Python installed, then run:

```bash
pip install requests

```

### 3. Configuration

Open `sport_bot.py` in your text editor and replace the placeholder strings with your actual credentials:

| Variable | Description | Source |
| --- | --- | --- |
| `API_KEY` | Your unique API Key | [RapidAPI Dashboard](https://rapidapi.com/api-sports/api/api-football) |
| `TELEGRAM_TOKEN` | The Bot Token | [@BotFather](https://t.me/botfather) |
| `CHAT_ID` | Your Personal ID | [@userinfobot](https://t.me/userinfobot) |

### 4. Run the Bot

Execute the script to start monitoring:

```bash
python3 sport_bot.py

```

---

## ⚠️ Disclaimer

**Educational and Statistical Use Only.** This tool is designed for data analysis and logic testing. It **does not guarantee financial gain** or winning bets. Gambling involves risk; this bot should not be used as the sole basis for any financial decision. **Please play responsibly.**
