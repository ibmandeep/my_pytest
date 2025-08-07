import math

from source.shapes import Circle

class TestCircle:
    def setup_method(self, method):
        """This will run before each test"""
        self.circle = Circle(10)
    
    def test_area(self):
        radius = self.circle.radius
        assert self.circle.area() == math.pi * (radius ** 2)
        
    def test_perimeter(self):
        radius = self.circle.radius
        assert self.circle.perimeter() == 2 * math.pi * radius   

    def teardown_method(self, method):
        """This will run after each test"""
        del self.circle