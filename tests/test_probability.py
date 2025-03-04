import pandas as pd


def test_fraction_of_bankers():
    gss = pd.read_csv("tests/data/gss_bayes.csv")
    obtained = get_frsaction_of_bankers(gss)
    assert obtained < 1
