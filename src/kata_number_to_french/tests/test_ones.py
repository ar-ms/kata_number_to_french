from ..main import process


def test_one():
    assert process(1) == "un"


def test_eleven():
    assert process(11) == "onze"


def test_twenty_one():
    assert process(21) == "vingt-et-un"


def test_seventy_one():
    assert process(71) == "soixante-et-onze"


def test_ninety_one():
    assert process(91) == "quatre-vingt-onze"


def test_eigthy_one():
    assert process(81) == "quatre-vingt-un"


def test_eigthy_hundred_and_one():
    assert process(101) == "cent-un"
