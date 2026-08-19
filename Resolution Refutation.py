def resolve(c1, c2):
    resolvents = set()

    for lit1 in c1:
        for lit2 in c2:

            if lit1 == lit2[1:] and lit2.startswith("~"):
                resolvents.add((c1 - {lit1}) | (c2 - {lit2}))

            elif lit2 == lit1[1:] and lit1.startswith("~"):
                resolvents.add((c1 - {lit1}) | (c2 - {lit2}))

    return resolvents


def resolution(clauses, query):
    clauses = set(frozenset(c) for c in clauses)

    clauses.add(frozenset({"~" + query}))

    while True:
        new = set()
        clause_list = list(clauses)

        for i in range(len(clause_list)):
            for j in range(i + 1, len(clause_list)):

                for resolvent in resolve(clause_list[i], clause_list[j]):

                    if not resolvent:
                        return True

                    new.add(frozenset(resolvent))

        if new.issubset(clauses):
            return False

        clauses.update(new)


clauses = [
    {"P", "Q"},
    {"~Q", "R"},
    {"~P"}
]

query = "R"

print("Query proved:", resolution(clauses, query))