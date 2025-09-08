# Python Text-to-Speech (TTS) Engine

A hybrid Text-to-Speech (TTS) engine built with **Microsoft Edge Neural Voices (edge-tts)** for high-quality online speech synthesis and **pyttsx3** as an offline fallback. Audio playback is powered by **pygame**.

<!--- This project is part of **Darling AI** (Jarvis), an AI-powered text and voice assistant developed by **Ajay Dilip Yemmewar** (Final Year B.Tech CSE, YouTube: [@TheLearnLog](https://www.youtube.com/@TheLearnLog)). --->

---

## 🚀 Features
- ✅ Convert text into speech using Microsoft Edge Neural Voices (online).
- ✅ Fallback to `pyttsx3` (offline) when no internet is available.
- ✅ Smart long-text handling with polite summaries.
- ✅ Audio playback using `pygame`.
- ✅ Callback function support for early stopping.
- ✅ Modular and extensible design.

---

## 📂 Project Structure
```plaintext
tts-engine/
│
├── Data/               # Stores generated audio files (ignored in git)
│   └── .gitkeep
│
├── .env.example        # Example config file
├── .gitignore
├── LICENSE
├── main.py             # Entry point
├── README.md
└── requirements.txt
```
## ⚙️ Installation & Setup
1. Clone the repository
   ```
   git clone https://github.com/your-username/tts-engine.git
   cd tts-engine
2. Create a virtual environment (recommended)
   ```
   python -m venv venv
   source venv/bin/activate    # On Linux/Mac
   venv\Scripts\activate       # On Windows
3. Install dependencies
   ```
   pip install -r requirements.txt
4. Setup environment variables
   .env
   et your desired voice, e.g.:
   ```
   AssistantVoice=en-US-AriaNeural
5. Run the program:
   ```
   python main.py

## 🔧 Requirements
- Python 3.8+
- Internet (for edge-tts, otherwise offline mode will be used).
-- Dependencies:
   - pygame – audio playback
   - edge-tts – online TTS
   - pyttsx3 – offline TTS
   - python-dotenv – env variable management
- 🚫 Built-in Python standard library (no need to install or add to requirements.txt) - random, asyncio, os and pathlib

## 📌 Use Cases
- AI assistants like Darling AI
- Chatbots with speech replies
- Accessibility tools for visually impaired users
- Interactive educational apps
- Kiosk and customer service bots
- Offline systems with limited internet

## 📜 License
This project is licensed under the MIT License – see [LICENSE](LICENSE) for details.

--- 

## 📫 Let's Connect
- 📧 Email: [ajay.dilip.yemmewar@gmail.com](mailto:ajay.dilip.yemmewar@gmail.com)
- 💼 LinkedIn: [Ajay Dilip Yemmewar](https://www.linkedin.com/in/ajay-dilip-yemmewar-b9b5372b3/)
- ✨ GitHub: [@AJAY010804](https://github.com/AJAY010804)
- 📺 YouTube: [@TheLearnLog](www.youtube.com/@TheLearnLog)

---

<p align="center">✨ Thanks for visiting! Let's learn, build, and grow together! ✨</p>

---
