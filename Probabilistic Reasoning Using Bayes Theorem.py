p_faulty = 0.10

p_positive_given_faulty = 0.90

p_positive_given_good = 0.05

p_good = 1 - p_faulty

p_positive = (
    p_positive_given_faulty * p_faulty
    + p_positive_given_good * p_good
)

p_faulty_given_positive = (
    p_positive_given_faulty * p_faulty
) / p_positive

print(
    "P(Faulty | Positive) =",
    round(p_faulty_given_positive, 4)
)

print(
    "Percentage =",
    round(p_faulty_given_positive * 100, 2),
    "%"
)