# __tracebackhide__ = True is a special internal variable used in pytest to hide parts of the traceback in test failure
#  reports. It is not a Python keyword but a convention used by pytest to improve the clarity of test output.

def helper(x, y):
    __tracebackhide__ = True
    assert x == y, f"{x} != {y}"

def test_numbers():
    helper(1, 2)