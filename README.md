HEAD
# arcade-gcal-demo

This repo contains hands-on experiments with the **Google Calendar API** to validate
event creation, update (PATCH), and deletion behavior using native Google APIs.

## Why this repo exists

- Arcade Google Calendar integration update/delete did not persist reliably
- Verified behavior using **direct Google Calendar API**
- Proved that `events.patch` and `events.delete` work correctly with OAuth

## What is covered

- OAuth re-auth flow using Desktop client
- Fetching events by ID
- Updating events using `events.patch`
- Deleting events using `events.delete`
- Verifying updates directly in Google Calendar UI

## Key scripts

- `gcal_patch.py` – Update event title using Google Calendar API
- `gcal_delete.py` – Delete an event using Google Calendar API
- `debug_delete.py` – Verify ownership and deletion behavior
- `reauth_and_create.py` – OAuth re-auth + event creation
- `list_*` scripts – Event verification and debugging helpers

## Tech stack

- Python 3.12
- google-api-python-client
- google-auth / google-auth-oauthlib
- OAuth 2.0 Desktop flow

## Notes

- OAuth credentials and tokens are intentionally excluded from git
- This repo is intended for experimentation and pipeline validation
- Next step: expose these operations as API endpoints with clear payloads


a4c59e5 (Google Calendar API experiments: patch, delete, verification)
