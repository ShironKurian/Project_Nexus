import pytest
from datetime import datetime

def test_date_formatting():
    """Test date formatting utility"""
    test_date = datetime(2023, 1, 1)
    formatted_date = test_date.strftime("%Y-%m-%d")
    assert formatted_date == "2023-01-01"

def test_string_validation():
    """Test string validation utility"""
    test_string = "Hello World"
    assert len(test_string) > 0
    assert isinstance(test_string, str)

def test_number_validation():
    """Test number validation utility"""
    test_number = 42
    assert isinstance(test_number, int)
    assert test_number > 0 