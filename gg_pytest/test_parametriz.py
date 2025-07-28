import pytest

def add(num1, num2): 
    return num1 + num2

@pytest.mark.parametrize("num1, num2, res", [(1,2,3), (5,5,10), (9,8, 17), (3,4,7)])
def test_add(num1, num2, res):
    assert add(num1, num2) == res