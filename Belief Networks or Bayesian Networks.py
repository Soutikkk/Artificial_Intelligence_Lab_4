p_cloudy = {
    True: 0.5,
    False: 0.5
}

p_rain_given_cloudy = {
    True: {
        True: 0.8,
        False: 0.2
    },
    False: {
        True: 0.2,
        False: 0.8
    }
}

p_wet_given_rain = {
    True: {
        True: 0.9,
        False: 0.1
    },
    False: {
        True: 0.2,
        False: 0.8
    }
}


def joint_probability(cloudy, rain, wet):

    p1 = p_cloudy[cloudy]

    p2 = p_rain_given_cloudy[cloudy][rain]

    p3 = p_wet_given_rain[rain][wet]

    return p1 * p2 * p3


numerator = 0

for cloudy in [True, False]:
    numerator += joint_probability(cloudy, True, True)


denominator = 0

for cloudy in [True, False]:

    for rain in [True, False]:

        denominator += joint_probability(cloudy, rain, True)


posterior = numerator / denominator

print("P(Rain | WetGrass) =", round(posterior, 4))

print("Percentage =", round(posterior * 100, 2), "%")