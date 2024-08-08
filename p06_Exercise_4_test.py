import sys
import os
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))

from p06_Exercise_4 import *

def test_func():
    mock = MagicMock(return_value="1")
    with patch('p06_Exercise_4._get_data', mock):
        assert get_avg(1) == 1
    mock = MagicMock(return_value="12")
    with patch('p06_Exercise_4._get_data', mock):
        assert get_avg(2) == 1.5
    mock = MagicMock(return_value="123")
    with patch('p06_Exercise_4._get_data', mock):
        assert get_avg(3) == 2
    mock = MagicMock(return_value="1234")
    with patch('p06_Exercise_4._get_data', mock):
        assert get_avg(4) == 2.5
    mock = MagicMock(return_value="12345")
    with patch('p06_Exercise_4._get_data', mock):
        assert get_avg(5) == 3
    mock = MagicMock(return_value="123456")
    with patch('p06_Exercise_4._get_data', mock):
        assert get_avg(6) == 3.5
    mock = MagicMock(return_value="1234567")
    with patch('p06_Exercise_4._get_data', mock):
        assert get_avg(7) == 4
    mock = MagicMock(return_value="12345678")
    with patch('p06_Exercise_4._get_data', mock):
        assert get_avg(8) == 4.5
    mock = MagicMock(return_value="123456789")
    with patch('p06_Exercise_4._get_data', mock):
        assert get_avg(9) == 5
