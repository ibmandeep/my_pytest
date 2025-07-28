import pytest
import math




@pytest.fixture
def input_value():
    input = 8
    return input



def test_diff(input_value):
    assert 10 - 2 == input_value


def test_sqr(input_value):
    assert input_value == math.sqrt(64)