# Q1 – Design decision and alternative concepts

## Predictions before execution

| Household | Units | Ration card? | Oldest age | Predicted correct decision |
|---|---:|---|---:|---|
| H1 | 100 | No | 30 | Full subsidy |
| H2 | 100 | Yes | 83 | Full subsidy only |
| H3 | 101 | Yes | 35 | Partial subsidy |
| H4 | 101 | No | 85 | No subsidy |
| H5 | 200 | Yes | 50 | Partial subsidy |
| H6 | 200 | No | 82 | No subsidy |
| H7 | 201 | No | 81 | Elderly exception subsidy |
| H8 | 201 | No | 80 | No subsidy (the rule says above 80) |

The assignment does not provide subsidy amounts, so the program reports the decision category and does not invent a rupee value.

## Why separate if statements can overlap

Each separate `if` is checked independently. If more than one condition is true, more than one result can be appended. In the deliberately faulty example, the partial-subsidy condition is `units <= 200 and has_ration_card`; this also matches a household at exactly 100 units. H2 therefore receives both Full subsidy and Partial subsidy. Adding the lower boundary (`101 <= units <= 200`) would prevent that overlap.

With `if-elif-else`, Python stops after the first matching branch. The corrected conditions are ordered and mutually exclusive, so exactly one decision is returned.

## Design decision: combined conditions

Use an `if-elif-else` chain with clear chained comparisons and `and`. It reads like the three policy slabs and avoids deep nesting. A nested `if` is also valid (for example, check the units slab first, then check ration-card status inside the 101–200 slab), but the combined conditions are shorter for these three rules. If the rules later gain more tests inside a slab, nested conditions may become easier to maintain.

## Alternative: match-case

Python 3.10+ supports `match`. The match version can use guarded cases such as `case n if n <= 100`, `case n if 101 <= n <= 200 and has_ration_card`, and `case n if n > 200 and oldest_member_age > 80`. It still selects one branch. The time per decision is O(1) for this fixed number of cases, and extra space is O(1).

## Alternative: list of upper-limit rules

A table can store limits and a label, then a loop can search the table. For k slabs, a simple sequential search takes O(k) time in the worst case and O(k) space for the table. A small fixed slab table is easy to revise without changing several conditions, but a final special elderly rule still needs a separate Boolean check. An `if-elif-else` chain has O(1) time for this fixed three-slab problem and O(1) extra space.
