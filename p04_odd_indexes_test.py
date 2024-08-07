import pytest
from .p04_odd_indexes import odd_indexes


def test_odd_indexes_str():
    assert odd_indexes("elephant") == "lpat"
    assert odd_indexes("computer") == "optr"


def test_odd_indexes_int():
    assert odd_indexes("5578") == "58"
    assert odd_indexes("87158971") == "7591"


@pytest.mark.parametrize("input, output", [
    ("elephant", "lpat"), ("computer", "optr"), ("5578", "58"), ("87158971", "7591")])
def test_odd_indexes(input, output):
    assert odd_indexes(input) == output
