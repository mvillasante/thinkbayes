def conditional(a, given):
    return prob(a & given) / prob(given)


def prob(a):
    return a.mean()


def get_fraction_of_bankers(data):
    banker = data["indus10"] == 6870
    return prob(banker)
