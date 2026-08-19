facts = {
    ("student", "Asha"),
    ("student", "Ravi"),
    ("programmer", "Ravi"),
    ("programmer", "Mina")
}

rules = [
    ("student", "programmer", "learner")
]


def extract_answers(predicate):

    answers = []

    for relation, person in facts:

        if relation == predicate:
            answers.append((person, "direct fact"))

    for source_pred, target_pred, derived_pred in rules:

        if predicate == derived_pred:

            for relation, person in facts:

                if relation == source_pred:

                    if (target_pred, person) in facts:
                        answers.append(
                            (person, f"derived from {source_pred} and {target_pred}")
                        )

    return answers


for query in ["student", "learner", "programmer"]:

    print("\nQuery:", query)

    for person, evidence in extract_answers(query):
        print(person, "->", evidence)