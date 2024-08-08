import random

import pytest
from .p01_BasicCalculator import BasicCalculator


class Test:

    def setup_method(self):
        print("\nEnvironment preparation for the test")
    def teardown_method(self):
        print("Cleaning of the environment after testing")
    def test_addition(self):
        basic_calculator = BasicCalculator()

        assert basic_calculator.add(1, 1) == 2
        assert basic_calculator.add(0, 1) == 1
        assert basic_calculator.add(0, 0) == 0
        assert basic_calculator.add(-2, -1) == -3
        assert basic_calculator.add(5, -3) == 2
        assert basic_calculator.add(-6, 1) == -5
        assert round(basic_calculator.add(1.1, 2.2), 2) == 3.3
        assert basic_calculator.add("Hello", "World") is None
        assert basic_calculator.add("desať", 1) is None
        assert basic_calculator.add(0, "sedem") is None

    def test_subtract(self):
        basic_calculator = BasicCalculator()

        assert basic_calculator.subtract(1, 1) == 0
        assert basic_calculator.subtract(0, 1) == -1
        assert basic_calculator.subtract(0, 0) == 0
        assert basic_calculator.subtract(-2, -1) == -1
        assert basic_calculator.subtract(5, -3) == 8
        assert basic_calculator.subtract(-6, 1) == -7
        assert round(basic_calculator.subtract(1.1, 2.2), 2) == -1.1
        assert basic_calculator.subtract("Hello", "World") is None
        assert basic_calculator.subtract("desať", 1) is None
        assert basic_calculator.subtract(0, "sedem") is None

    # @pytest.mark.skip(reason="skipping this test") # prekočíme multiply
    def test_multiply(self):
        basic_calculator = BasicCalculator()

        assert basic_calculator.multiply(1, 1) == 1
        assert basic_calculator.multiply(0, 1) == 0
        assert basic_calculator.multiply(0, 0) == 0
        assert basic_calculator.multiply(-2, -1) == 2
        assert basic_calculator.multiply(5, -3) == -15
        assert basic_calculator.multiply(-6, 1) == -6
        assert round(basic_calculator.multiply(1.1, 2.2), 2) == 2.42
        assert basic_calculator.multiply("Hello", "World") is None
        assert basic_calculator.multiply("desať", 1) is None
        assert basic_calculator.multiply(0, "sedem") is None

    def test_divide(self):
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
        assert round(basic_calculator.divide(1.1, 2.2), 2) == 0.5
        assert basic_calculator.divide("Hello", "World") is None
        assert basic_calculator.divide("desať", 1) is None
        assert basic_calculator.divide(0, "sedem") is None

        num1 = random.randint(1, 10000)
        num2 = random.randint(1, 10000)
        assert basic_calculator.multiply(num1, num2) > 0
        assert basic_calculator.multiply(-1 * num1, num2) < 0
        assert basic_calculator.multiply(num1, -1 * num2) < 0
        assert basic_calculator.multiply(-1 * num1, -1 * num2) > 0
