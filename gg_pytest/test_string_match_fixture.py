import pytest


@pytest.fixture
def string_match():
    string = "         Mandeep Singh     "
    return string.strip()


def test_remove_M(string_match):
    assert string_match.replace("M", "") == "andeep Singh"

def test_remove_D(string_match):
    assert string_match.replace('d', '') == "Maneep Singh"    