import pytest
import time
from source.my_function import add
from _pytest.assertion.rewrite import AssertionRewritingHook



def test_add():
    assert add(1,2) == 3


def test_addd():
    assert add(1,3) == 3

#pytest -m slow
#we can pass resoan as a arrg


@pytest.mark.slow
def test_slow_add():
    time.sleep(3)
    assert add(1,2) == 3

#pytest -m skip
@pytest.mark.skip
def test_skip_add():
    assert add(1,2) == 3    

#pytest -m xfail
@pytest.mark.xfail
def test_fail_add():
    assert add(1,2) == 4

