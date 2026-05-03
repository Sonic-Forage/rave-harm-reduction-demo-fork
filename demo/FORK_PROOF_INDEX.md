# Demo Fork Proof Index

This index maps the finished demo fork artifacts to repo-local proof, source discipline, and closed safety gates. It is a review aid for builders who want to fork the Sonic Forage harm-reduction community kit without claiming medical/legal authority or opening any public/offline lane.

> Status: `closed_until_human_yes`. This is a fictional/public-safe education demo. It is not medical advice, legal advice, emergency response training, field-operations authorization, fundraising copy, outreach approval, or a real private event plan.

## Proof map

| Proof lane | Artifact | What it demonstrates | Source / citation discipline | Closed gate reminder |
| --- | --- | --- | --- | --- |
| Finished city chapter | `demo/EXAMPLE_CITY_CHAPTER.md` | A fork can adapt upstream prompts into a fictional city chapter without using private event details. | Keep claims aligned to `docs/sources/SOURCES.md`; replace placeholders with official public URLs only after human review. | Do not publish private event locations, promise services, or represent a real organizer without approval. |
| Care-team summary | `demo/CARE_TEAM_ONE_PAGER.md` | A concise educational one-pager can use nonjudgmental, source-backed language. | Use National Harm Reduction Coalition principles, SAMHSA overdose education, and DanceSafe education as references; keep local claims review-only. | Do not diagnose, prescribe, certify, train, or imply guaranteed safety. |
| Replication checklist | `demo/FORK_REPLICATION_CHECKLIST.md` | Another builder can copy the fork pattern step-by-step with checks before any external action. | Require verifier runs and public-source review before a fork claims readiness. | No outreach, fundraising, payment links, field operations, or public posting without human yes. |
| Source correction example | `demo/SOURCE_CORRECTION_EXAMPLE.md` | A GitHub issue body can request better citations without turning into advice or private logistics. | Include exact quote/path, replacement wording, and official public source URL. | Do not include private media, private event details, medical/legal instructions, or service promises. |
| City resource directory template | `demo/CITY_RESOURCE_DIRECTORY_TEMPLATE.md` | A public-resource directory can be prepared using only official public URLs/source owners. | Every entry needs an official public URL, source owner, date checked, and scope note. | Do not publish private logistics, referral guarantees, emergency coverage promises, or field commitments. |
| Lesson receipt | `demo/LESSON_RECEIPT.md` | The fork documents exactly what changed from upstream and what remains closed. | Receipt should cite upstream repo and local verifier evidence rather than subjective claims. | Do not treat a clean receipt as approval to launch. |
| Verifiers | `scripts/verify.py`, `scripts/verify_demo.py` | The repo can automatically reject missing artifacts, missing safety strings, overclaims, and secret-like markers. | Keep future artifacts in the verifier once promoted to canonical demo proof. | Passing tests are readiness evidence only; approval remains `closed_until_human_yes`. |

## Human approval questions before any external action

1. Which exact public artifact, if any, is approved for posting or sharing?
2. Has a qualified human reviewed source wording, local legal context, and medical-emergency disclaimers?
3. Are all URLs official public URLs, with no private event location, private logistics, personal data, or unverified service promises?
4. Is any outreach, fundraising, payment link, field operation, private media upload, training/certification claim, or public launch explicitly approved in writing?
5. Who is the accountable human operator for takedown/correction requests after publication?

If any answer is missing or ambiguous, the lane stays closed.

## Re-run proof commands

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify.py
PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_demo.py
python3 -m py_compile scripts/verify.py scripts/verify_demo.py
git diff --check
```

Expected highlights:

- `HARM REDUCTION KIT VERIFY OK`
- `DEMO FORK VERIFY OK`
- no `SECRET-LIKE MARKER FOUND`
- no `UNSAFE OVERCLAIM FOUND`

## Blocked without explicit human approval

- Public posting or social sharing
- Direct outreach, DMs, email sends, calendar invites, or partnership asks
- Fundraising, payment links, sponsorship asks, or paid-service setup
- Field operations, staffing plans, private event location publication, or real-event logistics
- Medical advice, legal advice, diagnosis, prescribing, emergency-service replacement, or training/certification claims
- Private media upload, private dataset upload, GPU/video jobs, paid API calls, or spending
- Cron mutation, scheduling, or autonomous external execution

All blocked actions remain `closed_until_human_yes`.
