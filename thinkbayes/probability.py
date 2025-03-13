def bayes(a, b):
    """
    Theorem 3 "Bayes":
    """
    return prob(a) * conditional_probability(b, a) / prob(b)


def conditional_probability(a, given):
    """
    Theorem 1: conditional probability related to the probability of a conjunction.
    """
    return prob(a & given) / prob(given)


def conjunction_probability(a, b):
    """
    Theorem 2: the probability of a conjunction (prob(a & b))as conditional probability times probability.
    """
    return prob(b) * conditional_probability(a, b)


def prob(a):
    return a.mean()


def get_fraction_of_bankers(data):
    banker = data["indus10"] == 6870
    return prob(banker)
