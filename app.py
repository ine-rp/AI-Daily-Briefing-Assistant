from flask import Flask, jsonify, redirect, session, request, render_template
from dotenv import load_dotenv
from crew import crew
from utils.google_auth import get_google_flow, store_credentials_in_session, fetch_calendar_summary, fetch_gmail_summary
import os
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1" # remove this in production, only used for testing purposes

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev")  # for session encryption

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    flow = get_google_flow()
    auth_url, state = flow.authorization_url(prompt="consent", access_type="offline", include_granted_scopes="true")
    session["state"] = state
    return redirect(auth_url)

@app.route('/callback')
def callback():
    flow = get_google_flow()
    flow.fetch_token(authorization_response=request.url)

    creds = flow.credentials
    store_credentials_in_session(session, creds)
    return redirect("/briefing-ui")

@app.route('/briefing')
def briefing():
    email_summary = fetch_gmail_summary(session)
    calendar_summary = fetch_calendar_summary(session)

    print("\n🟡 EMAIL SUMMARY INPUT TO AGENT:")
    print(email_summary)

    print("\n🔵 CALENDAR SUMMARY INPUT TO AGENT:")
    print(calendar_summary)
    
    result = crew.kickoff(inputs={
        "emails_data": email_summary,
        "calendar_data": calendar_summary
    })

    print("Crew Result:", result)
    print("Crew Result (dir):", dir(result))

    return jsonify({
        "briefing": str(result)
    })

@app.route('/briefing-ui')
def briefing_ui():
    return render_template("briefing.html")

if __name__ == "__main__":
    app.run(debug=True)