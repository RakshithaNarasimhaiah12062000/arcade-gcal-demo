import webbrowser
from arcadepy import Arcade

client = Arcade()

# MUST match the Arcade account you authorized with
USER_ID = "narasimhaiahrakshitha0@gmail.com"

EVENT_ID = "utvtdv6748bbbn1ok1v6q7d7m0"

TOOL = "GoogleCalendar.DeleteEvent"

# Ensure authorization for delete
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
        "send_updates": "ALL"
    }
)

print("🗑️ Event deleted:", EVENT_ID)

