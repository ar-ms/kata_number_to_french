from ..main import process
from ..french_numbers import units


def test_zero():
    assert process(0) == "zéro"


def test_units():
    number_units = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)
    for num, fr_translation in zip(number_units, units[1:]):
        assert process(num) == fr_translation
