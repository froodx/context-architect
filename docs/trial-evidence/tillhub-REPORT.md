# TillHub report (2026-11-22)

## What changed
- **Money is right.** FREESHIP orders were rejected and the stock report crashed (2 of 8 tests had always failed). Both work now. Totals are penny-exact (ADR 0001), promos never go below zero, and receipts add up.
- **Refunds pay what was paid, once.** Before, a refund recomputed list price plus VAT, ignoring promos and discounts, and could be repeated, paying out and restocking each time.
- **Stock can't go wrong.** Each order is checked and taken in one transaction. Negative or absurd quantities, discounts over 100% and bad JSON get a clear 400. A refunded order's lines can no longer attach themselves to the next order (found by the independent check).
- **Safe.** All SQL is parameterised (it was injectable from the search URL). Three unused dependencies with 11 known advisories are gone (pip-audit, 2026-11-22). The unused live payment key is out of source. SMTP settings come from the environment. A stalled client now holds the tills for at most about 10 s, not forever; a deliberately slow client still can (the server is single-threaded; threading it is the fix if that ever matters).
- **Cheaper to change (about 30% of effort).** All money maths is in `pricing.py`, with no VAT anywhere else. The README now runs. CI and lint config are in place. `AGENTS.md` gives every agent the rules, and checks enforce them: ruff S608 for SQL, a test for secrets in source.
- Tests: 8 tests with 2 failing became 39 passing, green three runs in a row, on a temp database. Tests used to wipe `tillhub.db`.

## Scorecard
| Line | Before | Now |
|---|---|---|
| 1 Runs, 2 Tests, 5 Deps, 6 Hotspots, 7 One way, 8 Efficient, 9 Explained, 10 Guarded | Red (8 Amber) | Green |
| 3 Checked on every change | Red | Waiting: CI file written but never run, as there is no remote (gate 6) |
| 4 Safe | Red | Waiting: rotation and auth (gates 1, 2) |

**Timeframe:** planned 2 to 3 sessions; used 1 of 5. Your review: about 20 minutes.

## Decisions needed (recommendation first)
1. **Rotate the payment key and the SMTP password now.** Both are in git history (`app.py`, `emailer.py` before a4a9dda). This is outside my bounds.
2. **ADR 0002: require a till token on POST.** I recommend approving it. If you consider the shop network trusted, say so instead.
3. **FREESHIP:** shipping is never charged, so the code just takes 4.99 off. Is that intended? Separately, unknown promo codes are silently ignored (now logged). Should they be refused?
4. **History scrub of the secrets:** not needed once they are rotated. I recommend skipping it.
5. **Live database check.** The old refund bug may already have mixed lines into later orders. Run this read-only shortlist: `SELECT o.id, o.total FROM orders o JOIN order_lines l ON l.order_id = o.id GROUP BY o.id HAVING SUM(l.price*l.qty)*1.2 > o.total + 0.01;`. It also lists genuine promo or discount orders (the database does not record which), so compare the shortlist with your till records. Any clean-up deletes data, so it needs your approval.
6. **Push to a host and require the `ci` check** on `main`.

## ADRs
- 0001 Money maths in Decimal in one module: Accepted (easy to reverse, charter section 4).
- 0002 Shared token for write endpoints: Proposed, waiting for you.

## Deliberately not done
A web framework or ORM, splitting `app.py` further, integer pence in the schema (would need a data migration), type checking, packaging and Docker. None of these fixes a pain we have evidence for. `scripts.seed` adds duplicates if run twice; that's minor and left as it is.

## Next
Nothing is in flight. Say "carry on" after deciding any of the gates above.
