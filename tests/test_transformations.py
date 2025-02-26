from thinkbayes.dummy import add_offset


def test_add_offset():
    augend = 1
    addend = 2
    expected = augend + addend
    obtained = add_offset(augend, addend)
    assert expected == obtained
