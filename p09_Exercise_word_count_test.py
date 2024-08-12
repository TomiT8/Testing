"""Počítání slov
Implementujte funkci word_count(s), která vrátí počet slov v daném řetězci.
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))

import pytest
from p09_Exercise_word_count import *


def test_word_count():
    assert word_count("Hello world") == 2
    assert word_count("This is a test") == 4
    assert word_count("One more test case") == 4
    assert word_count("") == 0
    assert word_count("Python is awesome!") == 3


if __name__ == "__main__":
    pytest.main()
