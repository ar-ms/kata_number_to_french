from ..main import process


def test_eigthy():
    assert process(80) == "quatre-vingts"


def test_eigthy_one():
    assert process(81) == "quatre-vingt-un"


def test_two_hundreds():
    assert process(200) == "deux-cents"


def test_two_hundred_and_one():
    assert process(201) == "deux-cent-un"


def test_one_million():
    assert process(1_000_000) == "un-million"


def test_deux_million():
    assert process(2_000_000) == "deux-millions"
