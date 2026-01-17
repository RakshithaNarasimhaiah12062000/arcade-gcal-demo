import webbrowser
from arcadepy import Arcade

client = Arcade()
USER_ID = "narasimhaiahrakshitha0@gmail.com"
EVENT_ID = "utvtdv6748bbbn1ok1v6q7d7m0"

TOOL = "GoogleCalendar.DeleteEvent"

# Authorize delete (in case permissions were not granted for this tool yet)
auth = client.tools.authorize(tool_name=TOOL, user_id=USER_ID)
if auth.status != "completed":
    print("Authorize delete in browser:")
    print(auth.url)
    try:
        webbrowser.open(auth.url)
    except Exception:
        pass
    client.auth.wait_for_completion(auth.id)

client.tools.execute(
    tool_name=TOOL,
    user_id=USER_ID,
    input={
        "event_id": EVENT_ID,
        "calendar_id": "primary",
        "send_updates": "NONE"
    }
)

print("🗑️ Deleted:", EVENT_ID)

