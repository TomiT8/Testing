import random

import pytest
from .p01_BasicCalculator import BasicCalculator


def test_addition():
    basic_calculator = BasicCalculator()

    assert basic_calculator.add(1, 1) == 2
    assert basic_calculator.add(0, 1) == 1
    assert basic_calculator.add(0, 0) == 0
    assert basic_calculator.add(-2, -1) == -3
    assert basic_calculator.add(5, -3) == 2
    assert basic_calculator.add(-6, 1) == -5
    assert round(basic_calculator.add(1.1, 2.2),2) == 3.3
    assert basic_calculator.add("Hello", "World") is None
    assert basic_calculator.add("desať", 1) is None
    assert basic_calculator.add(0, "sedem") is None

@pytest.mark.parametrize("num1, num2, result",
                        [(5,7,12),(7,5,12),(15,0,15),(9,-5,4),(1,1,2),(-5,-3,-8),("5",2,None),(5,"ahoj",None),("hello","world",None)])
def test_adition2(num1,num2,result):
    basic_calculator = BasicCalculator()
    assert basic_calculator.add(num1,num2)==result

def test_subtract():
    basic_calculator = BasicCalculator()

    assert basic_calculator.subtract(1, 1) == 0
    assert basic_calculator.subtract(0, 1) == -1
    assert basic_calculator.subtract(0, 0) == 0
    assert basic_calculator.subtract(-2, -1) == -1
    assert basic_calculator.subtract(5, -3) == 8
    assert basic_calculator.subtract(-6, 1) == -7
    assert round(basic_calculator.subtract(1.1, 2.2),2) == -1.1
    assert basic_calculator.subtract("Hello", "World") is None
    assert basic_calculator.subtract("desať", 1) is None
    assert basic_calculator.subtract(0, "sedem") is None

def test_multiply():
    basic_calculator = BasicCalculator()

    assert basic_calculator.multiply(1, 1) == 1
    assert basic_calculator.multiply(0, 1) == 0
    assert basic_calculator.multiply(0, 0) == 0
    assert basic_calculator.multiply(-2, -1) == 2
    assert basic_calculator.multiply(5, -3) == -15
    assert basic_calculator.multiply(-6, 1) == -6
    assert round(basic_calculator.multiply(1.1, 2.2),2) == 2.42
    assert basic_calculator.multiply("Hello", "World") is None
    assert basic_calculator.multiply("desať", 1) is None
    assert basic_calculator.multiply(0, "sedem") is None

def test_divide():
    basic_calculator = BasicCalculator()

    assert basic_calculator.divide(1, 1) == 1
    assert basic_calculator.divide(0, 1) == 0
    """with pytest.raises(ZeroDivisionError):
            assert basic_calculator.divide(5, 0) == 0   # FIXME
    with pytest.raises(ZeroDivisionError):
        assert basic_calculator.divide(0, 0) == 0  # FIXME"""
    assert basic_calculator.divide(5, 0) is None
    assert basic_calculator.divide(0, 0) is None
    assert basic_calculator.divide(-2, -1) == 2
    assert round(basic_calculator.divide(5, -3), 2) == -1.67
    assert basic_calculator.divide(-6, 1) == -6
    assert round(basic_calculator.divide(1.1, 2.2),2) == 0.5
    assert basic_calculator.divide("Hello", "World") is None
    assert basic_calculator.divide("desať", 1) is None
    assert basic_calculator.divide(0, "sedem") is None

    num1 = random.randint(1, 10000)
    num2 = random.randint(1, 10000)
    assert basic_calculator.multiply(num1, num2) > 0
    assert basic_calculator.multiply(-1*num1, num2) < 0
    assert basic_calculator.multiply(num1, -1*num2) < 0
    assert basic_calculator.multiply(-1*num1, -1*num2) > 0
