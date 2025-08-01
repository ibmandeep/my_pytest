from main import get_weather_details, add, divide
import pytest

def test_get_weather():
    assert get_weather_details(26) == 'Hot'
    assert get_weather_details(20) == 'Cold'


def test_add():
    assert add(1,2) == 3


def test_divide():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        assert divide(10,0)

def test_divide_n():
    with pytest.raises(ValueError):
        assert divide(10,0)

def test_divide_p():
    assert divide(10,2) == 5
