🧩 WordSeek - SMS & CLI Word Guessing Game
WordSeek is a fun and interactive 5-letter word guessing game inspired by Wordle. This project includes two different interfaces for playing the game:

📱 SMS Version (powered by Twilio and Flask)

💻 Command Line Interface (CLI) Version

Players receive feedback using emoji tiles:

🟩 Letter is correct and in the right position

🟨 Letter is in the word but in the wrong position

🟥 Letter is not in the word

🔧 Features
SMS Game (app.py)
Built with Flask and Twilio API

Users can play via text message

Persistent session management per user

Command /new starts a new game

Validates input length and word validity

CLI Game (wordseek.py)
Terminal-based gameplay

Real-time feedback after each guess

Simple and intuitive interface

🗂 Files Overview
app.py - Flask app for the SMS game using Twilio

wordseek.py - Console version of the game

words.txt - List of valid 5-letter words (required for both versions)

🚀 Getting Started
Prerequisites
Python 3.x

Flask

Twilio account (for SMS version)

A words.txt file with 5-letter words, one per line

Running the CLI Version
bash
Copy
Edit
python wordseek.py
Running the SMS Version
bash
Copy
Edit
python app.py
Ensure you have set up a Twilio number and configured the webhook to point to /message.

📬 Example SMS Flow
vbnet
Copy
Edit
User: /new
Bot: Game started! Guess the 5-letter word!
User: stare
Bot: 🟥🟨🟥🟥🟥 STARE
📄 License
This project is licensed under the MIT License.
