# Fork Replication Checklist

This checklist turns the finished demo fork into a repeatable, human-reviewable lesson for another city chapter, campus group, venue safety team, or nightlife collective.

> Safety note: this is educational, public-safe planning material. It is **not medical advice**, legal advice, emergency response training, or permission to use illegal substances. It does not publish real event locations, private logistics, field operations, outreach, fundraising, or training claims. Those actions stay **closed until human approval**.

## 1. Copy only the safe framework layer

Use the upstream kit as the starting point:

- canonical kit: `https://github.com/Sonic-Forage/rave-harm-reduction-community-kit`
- finished demo fork: `https://github.com/Sonic-Forage/rave-harm-reduction-demo-fork`
- actual finished branch proof: `https://github.com/TheMindExpansionNetwork/rave-harm-reduction-community-kit/tree/demo/finished-harm-reduction-build`

Do not copy private event details, volunteer rosters, medical histories, ticketing data, group chats, credentials, or private venue contacts into git.

## 2. Pick one local-safe lesson lane

Choose exactly one starter lane before editing:

- fictional city chapter example
- source-backed safer dance-space checklist
- community resource directory with public agency/source links only
- organizer preflight worksheet with no real event location
- care-team role explainer with no certification or medical authority claim

Avoid claims like “certified,” “prevents overdose,” “guarantees safety,” or “official medical training.”

## 3. Fill the payload with placeholders first

Start from `framework/payloads/harm-reduction-city.payload.example.json`.

Required placeholder discipline:

- use fictional names or broad public regions;
- keep tokens, private URLs, and passwords as `[REDACTED]` if a field is needed;
- use public source URLs only;
- leave all external-action gates as `closed_until_human_yes`.

## 4. Generate the three minimum demo artifacts

A finished fork lesson should contain:

1. `demo/EXAMPLE_CITY_CHAPTER.md` — source-backed public-safe local chapter sample.
2. `demo/CARE_TEAM_ONE_PAGER.md` — plain-language role summary that tells readers to call emergency services in emergencies.
3. `demo/LESSON_RECEIPT.md` — concise proof of what changed and what stayed closed.

Optional but recommended: add this checklist as `demo/FORK_REPLICATION_CHECKLIST.md` so another fork can copy the pattern without guessing.

## 5. Run local verification

From the repo root:

```bash
python3 scripts/verify.py
python3 scripts/verify_demo.py
python3 -m py_compile scripts/verify.py scripts/verify_demo.py
git diff --check
```

Expected highlights:

- `HARM REDUCTION KIT VERIFY OK`
- `DEMO FORK VERIFY OK`
- no unsafe overclaim, token marker, or missing source-backed disclaimer

## 6. Closed gates for a real community fork

These actions remain blocked without an awake human organizer’s explicit approval:

- public posting or outreach
- fundraising, sponsorships, payment links, or spending
- field operations, staffing promises, or volunteer dispatch
- medical/legal advice or training/certification claims
- publication of private event locations or logistics
- uploads of private media, datasets, rosters, or incident reports
- GPU/video jobs, paid APIs, or automated publishing

If approval is ambiguous, keep the fork in documentation-only mode.

## 7. Human review questions before any external action

Before moving beyond docs, ask and record:

- What exact public text/media/location would be released?
- Who is accountable for final review?
- Which source backs each health/safety statement?
- What remains private or redacted?
- What is the rollback path if a correction is needed?

A safe fork can still be complete while every external lane remains closed.
