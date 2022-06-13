import a

def test_01():
    X, Y = 80, 94
    actual = a.main(X, Y)
    expected = 2
    assert actual == expected


def test_02():
    X, Y = 1_000, 63
    actual = a.main(X, Y)
    expected = 0
    assert actual == expected


def test_03():
    X, Y = 270, 750
    actual = a.main(X, Y)
    expected = 48
    assert actual == expected
