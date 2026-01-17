from arcadepy import Arcade

client = Arcade()
USER_ID = "narasimhaiahrakshitha0@gmail.com"

EVENT_ID = "utvtdv6748bbbn1ok1v6q7d7m0"

resp = client.tools.execute(
    tool_name="GoogleCalendar.GetEvent",
    user_id=USER_ID,
    input={
        "event_id": EVENT_ID,
        "calendar_id": "primary"
    }
)

print(resp.output.value)

