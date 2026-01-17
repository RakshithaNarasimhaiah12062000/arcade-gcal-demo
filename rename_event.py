import webbrowser
from datetime import datetime
from arcadepy import Arcade

client = Arcade()
USER_ID = "narasimhaiahrakshitha0@gmail.com"
EVENT_ID = "utvtdv6748bbbn1ok1v6q7d7m0"

auth = client.tools.authorize(tool_name="GoogleCalendar.UpdateEvent", user_id=USER_ID)
if auth.status != "completed":
    print(auth.url)
    try:
        webbrowser.open(auth.url)
    except Exception:
        pass
    client.auth.wait_for_completion(auth.id)

stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
client.tools.execute(
    tool_name="GoogleCalendar.UpdateEvent",
    user_id=USER_ID,
    input={
        "event_id": EVENT_ID,
        "calendar_id": "primary",
        "updated_summary": f"SHOULD DISAPPEAR {stamp}",
        "send_notifications_to_attendees": "NONE",
    },
)

print("Renamed event. Now refresh Google Calendar UI and check the title.")

