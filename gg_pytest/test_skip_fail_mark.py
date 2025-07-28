import math
import pytest

# first test case
@pytest.mark.skip
def test_floor():
   num = 7
   assert num==math.floor(6.34532)

# second test case
def test_equal():
   assert 50 == 49

# third test case
@pytest.mark.xfail
def test_difference():
   assert 99-43==57

# fourth test case
def test_square_root():
   val=8
   assert val==math.sqrt(81)