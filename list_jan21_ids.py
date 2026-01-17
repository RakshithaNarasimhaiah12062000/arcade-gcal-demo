import webbrowser
from arcadepy import Arcade

client = Arcade()
USER_ID = "narasimhaiahrakshitha0@gmail.com"

TOOL = "GoogleCalendar.ListEvents"

# Authorize ListEvents (required)
auth = client.tools.authorize(tool_name=TOOL, user_id=USER_ID)
if auth.status != "completed":
    print(auth.url)
    try:
        webbrowser.open(auth.url)
    except Exception:
        pass
    client.auth.wait_for_completion(auth.id)

resp = client.tools.execute(
    tool_name=TOOL,
    user_id=USER_ID,
    input={
        "calendar_id": "primary",
        "min_end_datetime": "2026-01-21T00:00:00",
        "max_start_datetime": "2026-01-21T23:59:59",
        "max_results": 10,
    }
)

for e in resp.output.value.get("events", []):
    if e.get("summary") == "Arcade reauth test event":
        print("TITLE:", e.get("summary"))
        print("START:", e.get("start"))
        print("EVENT_ID:", e.get("id"))
        print("STATUS:", e.get("status"))
        print("---- FULL EVENT ----")
        print(e)
        print("-" * 40)

