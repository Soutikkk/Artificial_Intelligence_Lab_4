facts = {"rain", "cloudy"}

rules = [
    ({"rain"}, "wet_ground"),
    ({"wet_ground", "cloudy"}, "slippery_road"),
    ({"slippery_road"}, "drive_carefully")
]

changed = True

while changed:
    changed = False

    for premises, conclusion in rules:
        if premises.issubset(facts) and conclusion not in facts:
            facts.add(conclusion)
            changed = True

print("All known and inferred facts:")

for fact in sorted(facts):
    print("-", fact)