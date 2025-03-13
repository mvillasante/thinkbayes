from thinkbayes.probability import get_fraction_of_bankers, prob, conditional_probability

import pandas as pd
import pytest


gss = pd.read_csv("tests/data/gss_bayes.csv")


banker = gss["indus10"] == 6870


def test_fraction_of_bankers():
    obtained = get_fraction_of_bankers(gss)
    assert obtained == 0.014769730168391155
    assert prob(banker) == 0.014769730168391155


party_index = 1
democrat = gss.partyid <= party_index

polviews_index = 3
liberal = gss["polviews"] <= polviews_index


female = gss["sex"] == 2


def test_prob_features():
    assert prob(female) == 0.5378575776019476

    assert prob(liberal) == 0.27374721038750255

    assert prob(democrat) == 0.3662609048488537


def test_conjuntion():
    """
    probability that a respondent is a banker and a Democrat
    """
    assert prob(banker & democrat) == 0.004686548995739501


def test_conditional_probability():
    """
    probability that a respondent is a Democrat given that they are a liberal
    """
    selected = democrat[liberal]
    assert prob(selected) == 0.5206403320240125
    obtained = conditional_probability(liberal, given=female)
    assert pytest.approx(obtained, 1e-6) == 0.27581004111500884
    prob_female_respondent_given_liberal_and_Democrat = conditional_probability(
        female, given=liberal & democrat
    )
    assert prob_female_respondent_given_liberal_and_Democrat == 0.576085409252669
    prob_female_liberal_given_banker = conditional_probability(liberal & female, given=banker)
    assert prob_female_liberal_given_banker == 0.17307692307692307
