def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True



import pytest

@pytest.mark.parametrize("num, result", [(1, False), (2, True), (3, True), (4, False), (17, True)])
def test_is_prime(num, result):
    assert is_prime(num) == result