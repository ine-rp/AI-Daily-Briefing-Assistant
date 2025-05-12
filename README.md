# AI Daily Briefing Assistant

A multi-agent system that connects to your **Gmail** and **Google Calendar**, summarizes your unread emails and today’s events, and delivers a personalized daily briefing — all powered by **CrewAI**, **Gemini**, and connected through **Flask**.

🎯 Built as a portfolio project to showcase agent orchestration, API integration, and minimal web UI.


## 📋 Features

- ✅ Google OAuth login (Gmail + Calendar access)
- 🧾 Summarizes today’s unread emails
- 📆 Lists all calendar events scheduled for today
- 🤖 Powered by multiple LLM agents using [CrewAI](https://docs.crewai.com)
- 🌐 Clean, responsive frontend (HTML + JS)
- 🔒 Secure token storage in Flask session
- ⚡ Fast, async-friendly task execution


## 🏗️ Folder Structure

```markdown
ai-daily-briefing/
├── app.py                  # Flask app with all routes
├── crew.py                 # CrewAI setup with agents and tasks
├── agents/
│   ├── email_agent.py
│   ├── calendar_agent.py
│   └── summary_agent.py
├── tasks/
│   ├── summarize_emails.py
│   ├── analyze_calendar.py
│   └── compose_briefing.py
├── utils/
│   └── google_auth.py      # Google OAuth + API calls
├── templates/
│   ├── index.html
│   └── briefing-ui.html
├── credentials.json        # Google OAuth credentials (ignored in .gitignore)
├── .env                    # Contains your GEMINI_API_KEY (ignored in .gitignore)
└── README.md
```


## 🚀 Getting Started

### 1. Clone this repo

```bash
git clone https://github.com/yourusername/ai-daily-briefing.git
cd ai-daily-briefing
```
### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Add your secrets

Create a .env file:
```bash
GEMINI_API_KEY=your-openai-key
```
### 5. Run the app
```bash
python app.py
```

Open http://127.0.0.1:5000 to get started.


## 🧠 What I Learned
	•	How to build multi-agent workflows with CrewAI
	•	How to use Google APIs with secure OAuth
	•	How to connect real data to language models
	•	How to structure a clean, testable AI product from scratch



## 💻 Tech Stack
	•	CrewAI
	•	Gemini
	•	Flask
	•	Google Calendar API
	•	Gmail API


## License

MIT — feel free to fork and adapt for your own projects.
