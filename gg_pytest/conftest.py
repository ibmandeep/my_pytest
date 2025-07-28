import pytest

pytest_plugins = ["pytester"]

@pytest.fixture
def fun_name():
    name = "Mandeep"
    return name