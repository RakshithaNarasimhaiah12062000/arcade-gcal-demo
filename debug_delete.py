import webbrowser
from datetime import datetime
from arcadepy import Arcade

client = Arcade()

USER_ID = "narasimhaiahrakshitha0@gmail.com"  # <-- put your Arcade login email here
EVENT_ID = "utvtdv6748bbbn1ok1v6q7d7m0"
OWNER_CALENDAR = "narasimhaiahrakshitha0@gmail.com"  # from creator/organizer in your payload

def auth(tool):
    a = client.tools.authorize(tool_name=tool, user_id=USER_ID)
    if a.status != "completed":
        print(f"\nAuthorize {tool}:")
        print(a.url)
        try:
            webbrowser.open(a.url)
        except Exception:
            pass
        client.auth.wait_for_completion(a.id)

def list_day(calendar_id):
    auth("GoogleCalendar.ListEvents")
    r = client.tools.execute(
        tool_name="GoogleCalendar.ListEvents",
        user_id=USER_ID,
        input={
            "calendar_id": calendar_id,
            "min_end_datetime": "2026-01-21T00:00:00",
            "max_start_datetime": "2026-01-21T23:59:59",
            "max_results": 50,
        },
    )
    events = r.output.value.get("events", [])
    match = [e for e in events if e.get("id") == EVENT_ID]
    return match[0] if match else None

def update_event(calendar_id):
    auth("GoogleCalendar.UpdateEvent")
    stamp = datetime.now().strftime("%H:%M:%S")
    r = client.tools.execute(
        tool_name="GoogleCalendar.UpdateEvent",
        user_id=USER_ID,
        input={
            "event_id": EVENT_ID,
            "calendar_id": calendar_id,
            "updated_summary": f"UPDATED-DEBUG {stamp}",
            "send_notifications_to_attendees": "NONE",
        },
    )
    return r.output.value

def delete_event(calendar_id):
    auth("GoogleCalendar.DeleteEvent")
    r = client.tools.execute(
        tool_name="GoogleCalendar.DeleteEvent",
        user_id=USER_ID,
        input={
            "event_id": EVENT_ID,
            "calendar_id": calendar_id,
            "send_updates": "ALL",
        },
    )
    return r.output.value

for cal in ["primary", OWNER_CALENDAR]:
    print("\n==============================")
    print("Calendar:", cal)

    before = list_day(cal)
    print("Before delete - found?" , bool(before))
    if before:
        print("Summary:", before.get("summary"))
        print("Creator:", before.get("creator"))
        print("Organizer:", before.get("organizer"))

        print("\nTrying UPDATE to confirm it really exists...")
        try:
            out = update_event(cal)
            print("Update OK:", out)
        except Exception as e:
            print("Update failed:", repr(e))

        print("\nTrying DELETE...")
        try:
            out = delete_event(cal)
            print("Delete OK:", out)
        except Exception as e:
            print("Delete failed:", repr(e))

        after = list_day(cal)
        print("\nAfter delete - found?" , bool(after))
        if after:
            print("Still present summary:", after.get("summary"))
    else:
        print("Event not found on this calendar.")

