import pytest
import source.shapes as shape

@pytest.fixture
def square():
    square = shape.Square(10)
    return square

@pytest.fixture
def other_square():
    square = shape.Square(4)
    return square
