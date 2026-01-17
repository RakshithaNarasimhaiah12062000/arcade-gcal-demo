from arcadepy import Arcade

client = Arcade()
USER_ID = "narasimhaiahrakshitha0@gmail.com"

resp = client.tools.execute(
    tool_name="GoogleCalendar.ListEvents",
    user_id=USER_ID,
    input={
        "calendar_id": "primary",
        "max_results": 20,
        "show_deleted": True
    }
)

found = False
for e in resp.output.value["events"]:
    if e["id"] == "utvtdv6748bbbn1ok1v6q7d7m0":
        found = True
        print("FOUND EVENT:")
        print(e)

if not found:
    print("✅ Event ID not found in calendar (it is deleted)")

