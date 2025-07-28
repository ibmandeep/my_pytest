import math

# first test case
def test_check_floor():
   num = 6
   assert num==math.floor(6.34532)

# second test case
def test_equal():
   assert 50 == 49

# third test case
def test_check_difference():
   assert 99-43==57

# fourth test case
def test_square_root():
   val=8
   assert val==math.sqrt(81)

# In this example, we have created a program that has four test cases, checking floor as function name test_check_floor, 
# equality as function name test_equal, subtraction as function name test_check_difference, and square root as 
# function name test_square_root. Here, two functions have checked as common substrings in their names, thus we will execute these test cases.

# Now, we will run the following command with substring_match as check as follows:
# pytest test_run_subtests.py -k check -v   
