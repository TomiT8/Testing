import pytest
from .p05_test_func import *


@pytest.mark.parametrize("number, result", [(12, 2), (11, 2), (2, 4), (123, 26), (92, 18), (79, 14), (19023, 206)])
def test_func(number, result):
    assert func(number) == result


# todo
#   doplnené pre precvičenie
def test_func2():
    assert func(12) == 2
    assert func(11) == 2
    assert func(2) == 4
    assert func(123) == 26
    assert func(92) == 18
    assert func(79) == 14
    assert func(19023) == 206
