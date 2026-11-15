"""Q1: Compare separate if statements with an if-elif-else decision."""


def separate_if_decision(units, has_ration_card, oldest_member_age):
    """Show how separate if statements can accidentally give two results."""
    decisions = []

    # The first rule is correct, but the second condition is too broad.
    # At 100 units, a ration-card holder can receive both results.
    if units <= 100:
        decisions.append("Full subsidy")

    if units <= 200 and has_ration_card:
        decisions.append("Partial subsidy")

    if units > 200 and oldest_member_age > 80:
        decisions.append("Elderly exception subsidy")

    if len(decisions) == 0:
        decisions.append("No subsidy")

    return decisions


def elif_decision(units, has_ration_card, oldest_member_age):
    """Return exactly one subsidy decision using mutually exclusive branches."""
    if units <= 100:
        return "Full subsidy"
    elif 101 <= units <= 200 and has_ration_card:
        return "Partial subsidy"
    elif units > 200 and oldest_member_age > 80:
        return "Elderly exception subsidy"
    else:
        return "No subsidy"


households = [
    ("H1", 100, False, 30),
    ("H2", 100, True, 83),
    ("H3", 101, True, 35),
    ("H4", 101, False, 85),
    ("H5", 200, True, 50),
    ("H6", 200, False, 82),
    ("H7", 201, False, 81),
    ("H8", 201, False, 80),
]

print("Q1 - ELECTRICITY SUBSIDY DECISIONS")
print("ID  Units  Ration  Oldest age  Separate if result                 if-elif result")
for household_id, units, ration, age in households:
    separate = ", ".join(separate_if_decision(units, ration, age))
    correct = elif_decision(units, ration, age)
    print(f"{household_id:<3} {units:<6} {str(ration):<7} {age:<11} {separate:<34} {correct}")

print("\nBoundary checks: 100, 101, 200 and 201 units are all included.")
print("The separate-if example gives two results for H2 because its second test also accepts 100 units.")
