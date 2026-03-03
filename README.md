⚽ Football In-Play Red Card Alert Bot
An automated Telegram bot designed to detect high-value betting opportunities by monitoring red cards and live match statistics.

📖 Overview
This bot continuously scans live football data across major world leagues to identify specific match dynamics where a favorite remains dominant despite an opponent's red card.

The bot filters for:

Red Card Event: Only triggers when a player is sent off.

Ranking Gap: Only alerts if the team with the red card is ranked lower in the standings than their opponent.

Time Remaining: Only triggers if there are at least 20 minutes of play remaining (Minute < 70').

Dominance Metrics: Automatically pulls possession percentage and shot counts to confirm the favorite's dominance.

🚀 Key Features
Real-time Monitoring: Scans live matches every 5 minutes.

Smart Standings Integration: Automatically downloads league tables to determine the "underdog" vs the "favorite."

Telegram Notifications: Instant alerts delivered directly to your phone with Markdown formatting.

Wide League Coverage: Pre-configured for Serie A, Premier League, La Liga, Bundesliga, Ligue 1, and more.

📊 Sample Alert
Plaintext
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
🛠 Tech Stack
Language: Python 3.x

API Provider: API-Football (V3)

Notification Engine: Telegram Bot API

Libraries: requests

⚙️ Setup & Installation
Clone the Repository: Ensure your repository is set to Private.

Install Dependencies:

Bash
pip install requests
Configuration: Edit the sport_bot.py file and insert your credentials:

API_KEY: Your RapidAPI Key.

TELEGRAM_TOKEN: Provided by @BotFather.

CHAT_ID: Your unique Telegram ID.

Run the Bot:

Bash
python3 sport_bot.py
⚠️ Disclaimer
This tool is for educational and statistical purposes only. It does not guarantee financial gain and should not be used as the sole basis for gambling decisions. Play responsibly.
