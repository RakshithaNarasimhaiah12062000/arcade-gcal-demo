from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os

SCOPES = ["https://www.googleapis.com/auth/calendar.events"]

CALENDAR_ID = "primary"
EVENT_ID = "utvtdv6748bbbn1ok1v6q7d7m0"  # your event id

def get_service():
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json", SCOPES
        )
        creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return build("calendar", "v3", credentials=creds)

service = get_service()

# GET the event (prove it exists)
event = service.events().get(
    calendarId=CALENDAR_ID,
    eventId=EVENT_ID
).execute()

print("Fetched event:", event.get("summary"))

# PATCH update (safe partial update)
updated = service.events().patch(
    calendarId=CALENDAR_ID,
    eventId=EVENT_ID,
    body={
        "summary": "UPDATED via direct Google API",
        "description": "PATCH update worked",
    },
    sendUpdates="none"
).execute()

print("Updated title:", updated.get("summary"))
print("Link:", updated.get("htmlLink"))

