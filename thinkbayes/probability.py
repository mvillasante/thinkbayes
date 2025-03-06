def get_fraction_of_bankers(data):
    banker = data["indus10"] == 6870
    return prob(banker)


def prob(a):
    return a.mean()
