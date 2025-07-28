import mathfuncs

def test_square():
    assert mathfuncs.Algebra.square(40) == 1600
    assert mathfuncs.Algebra.square(5) == 25

def test_cube():
    assert mathfuncs.Algebra.cube(40) == 64000
    assert mathfuncs.Algebra.cube(5) == 125

def test_is_triangle():
    assert mathfuncs.Geometry.is_triangle(120, 40, 20) == True
    assert mathfuncs.Geometry.is_triangle(45, 67, 99) == False

def test_is_quadrilateral():
    assert mathfuncs.Geometry.is_quadrilateral(350, 5, 5, 0) == True
    assert mathfuncs.Geometry.is_quadrilateral(11, 22, 33, 44) == False