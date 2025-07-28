import pytest

def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:
        def f():
            f()
        f()
    
    # assert "maximum recursion" in str(excinfo.value)


def myfucn():
    raise ValueError("Exception 123 raised")


def test_myfucn():
    with pytest.raises(ValueError, match=r".* 123 .*"):
        myfucn()