import pytest
import source.shapes as shape


# def test_area():
#     rectangle = shape.Rectangle(10, 20)
#     assert rectangle.area() == 10 * 20

# def test_perimeter():
#     rectangle = shape.Rectangle(10, 20)
#     assert rectangle.perimeter() == (2*10) + (2*20)    


@pytest.fixture
def rectangle():
    rectangle = shape.Rectangle(10, 20)
    return rectangle

@pytest.fixture
def other_rectangle():
    rectangle = shape.Rectangle(4, 5)
    return rectangle


def test_area(rectangle):
    assert rectangle.area() == 10 * 20

def test_perimeter(rectangle):
    assert rectangle.perimeter() == (2*10) + (2*20)    

def test_not_eq(rectangle, other_rectangle):
    assert rectangle != other_rectangle 