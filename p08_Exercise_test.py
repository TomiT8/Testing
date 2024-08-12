"""
Implementujte funkci is_prime(n), která vrátí True, pokud je číslo prvočíslo, jinak vrátí False.
Implementujte funkci factorial(n), která vrátí faktoriál čísla n.
"""

import sys
import os
from .p08_Exercise import *

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))


def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(17) == True
    assert is_prime(18) == False
    assert is_prime(19) == True


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120


if __name__ == "__main__":
    pytest.main()
