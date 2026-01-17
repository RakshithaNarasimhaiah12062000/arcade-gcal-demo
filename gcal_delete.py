from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import os

SCOPES = ["https://www.googleapis.com/auth/calendar.events"]

CALENDAR_ID = "primary"
EVENT_ID = "utvtdv6748bbbn1ok1v6q7d7m0"

if not os.path.exists("token.json"):
    raise RuntimeError("token.json not found. Run gcal_patch.py once to authenticate.")

creds = Credentials.from_authorized_user_file("token.json", SCOPES)
service = build("calendar", "v3", credentials=creds)

service.events().delete(
    calendarId=CALENDAR_ID,
    eventId=EVENT_ID,
    sendUpdates="none",
).execute()

print("🗑️ Deleted event:", EVENT_ID)

