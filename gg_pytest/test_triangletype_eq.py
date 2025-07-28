import pytest

# importing classes and function which we use in this file
from triangletype import OutOfRangeError
from triangletype import TriangleError
from triangletype import triangleType

# check if a < 10
def test_invalid_less_a():
    with pytest.raises(OutOfRangeError):
        triangleType(9, 20, 15)

# check if b < 10        
def test_invalid_less_b():
    with pytest.raises(OutOfRangeError):
        triangleType(20, 9, 15)
        
# check if c < 10        
def test_invalid_less_c():
    with pytest.raises(OutOfRangeError):
        triangleType(20, 15, 9)


# check if a > 50
def test_invalid_more_a():
    with pytest.raises(OutOfRangeError):
        triangleType(51, 30, 45)
        
# check if b > 50        
def test_invalid_more_b():
    with pytest.raises(OutOfRangeError):
        triangleType(30, 51, 45)
        
# check if c > 50        
def test_invalid_more_c():
    with pytest.raises(OutOfRangeError):
        triangleType(30, 45, 51)

# check if a, b, c can form a triangle or not        
def test_valid_invalidtriangle():
    with pytest.raises(TriangleError):
        triangleType(20, 15, 40)

# valid class - determines type of triangle        
def test_valid():
    assert triangleType(20, 15, 10) == "Scalene Triangle"