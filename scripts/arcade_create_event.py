import webbrowser
from arcadepy import Arcade

client = Arcade()
USER_ID = "narasimhaiahrakshitha0@gmail.com"

TOOL = "GoogleCalendar.CreateEvent"

auth = client.tools.authorize(tool_name=TOOL, user_id=USER_ID)
if auth.status != "completed":
    print("Open this URL to authorize:")
    print(auth.url)
    try:
        webbrowser.open(auth.url)
    except Exception:
        pass
    client.auth.wait_for_completion(auth.id)

print("✅ Authorized. Creating event...")

resp = client.tools.execute(
    tool_name="GoogleCalendar.CreateEvent",
    user_id=USER_ID,
    input={
        "summary": "Arcade reauth test event",
        "start_datetime": "2026-01-21T10:00:00",
        "end_datetime": "2026-01-21T10:30:00",
        "calendar_id": "primary",
        "description": "Created after reauth"
    }
)

print("🎉 Created:")
print(resp.output.value["event"]["id"])
print(resp.output.value["event"]["htmlLink"])

