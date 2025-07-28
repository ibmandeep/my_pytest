import pytest

# @pytest.mark.parametrize("test_input, result", [(3,3), (44,44), (90,90)])
# def test_eval(test_input, result):
#     assert test_input == result


# @pytest.mark.parametrize("test_input, result", [(3*3,9), (11*4,44), (10*9,90)])
# def test_eval(test_input, result):
#     assert test_input == result


@pytest.mark.parametrize(
    "test_input,expected",
    [("3+5", 8), ("2+4", 6), pytest.param("6*9", 42, marks=pytest.mark.xfail)],
)
def test_eval(test_input, expected):
    assert eval(test_input) == expected    




# Class

@pytest.mark.parametrize("n,expected", [(1, 2), (3, 4)])
class TestClass:
    def test_simple_case(self, n, expected):
        assert n + 1 == expected

    def test_weird_simple_case(self, n, expected):
        assert (n * 1) + 1 == expected


# # module
# # Apply parametrize to all functions below
# pytestmark = pytest.mark.parametrize("n, expected", [(1, 2), (3, 4)])

# def test_simple_case(n, expected):
#     assert n + 1 == expected

# def test_weird_case(n, expected):
#     assert (n * 1) + 1 == expected


@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_foo(x, y):
    print(f"x: {x} === y: {y}")
    assert x + y == x + y