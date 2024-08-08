import sys
import os

# Pridaj aktuálny adresár do sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))

from unittest.mock import patch, MagicMock
from p03_get_only_numbers import get_only_numbers, API

def test_read_only_numbers():
    test_data = ["1,4,5,25,aa,bb,23,4", "324,24,234www,1,23", "545,3w,32"]

    expected = "1|4|5|25|23|4|324|24|1|23|545|32"

    fake_api = MagicMock()
    fake_api.get_data.return_value = test_data
    with patch('p03_get_only_numbers.API', fake_api):
        result = get_only_numbers()
        assert result == expected
