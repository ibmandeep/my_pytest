import math

class TestCls:
    def setup_method(self, method):
        """This will run before each test"""
        #method = current test
        print("In Setup")
    
    def test_one(self):
        pass

    def test_two(self):
        assert True    

    def teardown_method(self, method):
        """This will run after each test"""
        print("In teardown")