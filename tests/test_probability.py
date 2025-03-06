from thinkbayes.probability import get_fraction_of_bankers, prob
import pandas as pd


gss = pd.read_csv("tests/data/gss_bayes.csv")


def test_fraction_of_bankers():
    obtained = get_fraction_of_bankers(gss)
    assert obtained == 0.014769730168391155
    bankers = gss["indus10"] == 6870
    assert prob(bankers) == 0.014769730168391155


def test_prob_features():
    female = gss["sex"] == 2
    assert prob(female) == 0.5378575776019476

    polviews_index = 3
    liberal = gss["polviews"] <= polviews_index
    assert prob(liberal) == 0.27374721038750255

    polviews_index = 1
    democrat = gss.partyid <= polviews_index
    assert prob(democrat) == 0.3662609048488537
