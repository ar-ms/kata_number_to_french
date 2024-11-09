import pytest
from ..main import process


def test_negative():
    with pytest.raises(ValueError):
        assert process(-1)


def test_billion():
    with pytest.raises(ValueError):
        process(1_000_000_000)
