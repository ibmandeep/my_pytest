from _pytest.outcomes import Failed

def custom_check(condition):
    if not condition:
        raise Failed("Custom failure reason")



Prefer using standard pytest functions like pytest.fail() when possible:
import pytest

def custom_check(condition):
    if not condition:
        pytest.fail("Custom failure reason")