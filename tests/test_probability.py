from thinkbayes.probability import get_fraction_of_bankers, prob
import pandas as pd


gss = pd.read_csv("tests/data/gss_bayes.csv")


def test_fraction_of_bankers():
    obtained = get_fraction_of_bankers(gss)
    assert obtained < 1


def test_prob_female():
    female = gss["sex"] == 2
    assert prob(female) == 0.5378575776019476
