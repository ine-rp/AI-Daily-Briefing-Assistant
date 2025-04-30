import os, flask, pathlib
import google.auth.transport.requests
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from dateutil.parser import parse
from datetime import datetime

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/calendar.readonly"
]

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
CLIENT_SECRETS_FILE = BASE_DIR / "credentials.json"

def get_google_flow():
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES,
        redirect_uri="http://127.0.0.1:5000/callback"
    )
    return flow

def is_today(event_time_str):
    event_date = parse(event_time_str).date()
    return event_date == datetime.now().date()

def get_credentials_from_session(session):
    if "credentials" not in session:
        return None
    return Credentials(**session["credentials"])

def store_credentials_in_session(session, creds):
    session["credentials"] = {
        "token": creds.token,
        "refresh_token": creds.refresh_token,
        "token_uri": creds.token_uri,
        "client_id": creds.client_id,
        "client_secret": creds.client_secret,
        "scopes": creds.scopes
    }

def fetch_gmail_summary(session):
    creds = get_credentials_from_session(session)
    if not creds:
        return "⚠️ Not logged in to Google."

    service = build("gmail", "v1", credentials=creds)
    response = service.users().messages().list(userId="me", labelIds=["INBOX"], maxResults=10).execute()

    messages = response.get("messages", [])
    summaries = []

    for msg in messages:
        msg_data = service.users().messages().get(userId="me", id=msg["id"]).execute()
        snippet = msg_data.get("snippet", "")
        summaries.append(snippet)

    return " ".join(summaries) if summaries else "No unread emails."

def fetch_calendar_summary(session):
    creds = get_credentials_from_session(session)
    if not creds:
        return "⚠️ Not logged in to Google."

    service = build("calendar", "v3", credentials=creds)
    now = datetime.utcnow().isoformat() + "Z"

    events_result = service.events().list(
        calendarId="primary",
        timeMin=now,
        maxResults=5,
        singleEvents=True,
        orderBy="startTime"
    ).execute()

    events = events_result.get("items", [])
    if not events:
        return "You have no events today."

    summary_lines = []
    for event in events:
        start = event["start"].get("dateTime", event["start"].get("date"))
        if is_today(start):
            summary_lines.append(f"{start}: {event.get('summary', 'No title')}")

    return "\n".join(summary_lines)