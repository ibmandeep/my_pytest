def test_area(square):
    assert square.area() == 10 ** 2

def test_perimeter(square):
    assert square.perimeter() == 4 * 10    

def test_not_eq(square, other_square):
    assert square != other_square 