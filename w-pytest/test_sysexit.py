import pytest

def f():
    raise SystemExit(1)

def add(num1, num2):
    return num1 + num2    

def test_mytest():
    with pytest.raises(SystemExit):
        f()    


@pytest.mark.parametrize("num1, num2, result", [(1,2,3), (5,5,10), (5,3,8)])
def test_add(num1, num2, result):
    assert add(num1, num2) == result