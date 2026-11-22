# Worked example | One reminder, two edits

Adapted from the Ari edition. This example uses a fictional calendar project and illustrative locators. It shows how evidence travels from a review into a decision, plan and hand-off.

**Brief.** An organiser can change a reminder’s time in the current editor. A colleague using an older editor can still change the title. Both edits must survive when they touch different fields.

**Review finding F1.** At illustrative revision `demo-a`, the old editor sends only the title. The update handler in `reminders/update.py::apply_edit` replaces the missing time with the default. In the example fixture, editing the title changes a 07:00 reminder to 09:00. This explains why someone can miss an appointment despite never changing its time. The fixture covers a missing field. The meaning of an explicit empty value needs a product decision.

**ADR-004, Proposed.** Omitted fields retain their stored values on update. A separate explicit action clears an optional field. Updating only the current editor would leave deployed clients exposed. Versioning the whole endpoint is possible but adds a second contract to maintain. The narrower change preserves the existing wire shape. Its cost is that stored defaults and explicit clearing now need distinct tests. The calendar maintainer owns the decision. Acceptance is pending.

| ID | Kind | Statement and links |
| --- | --- | --- |
| F1 | Knowledge / observation | Title-only edit changes the time. Supported-by the before/after fixture on demo-a. |
| I1 | Knowledge / invariant | Omitted fields retain stored values on update. Proposed for the reminders endpoint. |
| ADR-004 | Knowledge / decision | Would establish I1. Owned-by calendar maintainer. |
| T1 | State / task | Capture old-client behaviour at the public endpoint. Ready for a test worker. |
| T2 | State / task | Implement omission and clearing semantics. Depends-on T1 and acceptance of ADR-004. |
| T3 | State / task | Independently exercise title-only, explicit time and clear requests on the integrated revision. Depends-on T2. |

**Delivery.** While T1 proceeds, a read-only worker can inventory other callers sending explicit empty values. The implementer owns the update handler. The verifier receives the contract, client fixtures and integrated revision. Reverting code alone cannot recover reminder times already overwritten. Establish whether reliable history exists before proposing a repair.

**Hand-off.** Evidence in this example establishes the old behaviour. Verification of the proposed guarantee remains open until T3 returns actual results. A support worker can explain the visible change in one sentence: “Changing a reminder’s title will leave its time as you set it.”
