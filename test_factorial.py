from factorial import factorial
from factorial import InvalidArgumentException
from random import randint
import pytest

# Happy paths

# def test_factorial__return_the_factorial__when_the_number_is_positive_v1():
#    assert factorial(2) == 2

def test_factorial__return_the_number_one__when_the_number_is_one_v2():

    assert factorial(1) == 1

def test_factorail__return_the_number_six__when_the_number_is_three():

    assert factorial(3) == 6

def test_factorail__return_a_positive_number__when_the_number_is_positive():

    number = randint(1, 10)

    assert factorial(number) > 0 

def test_factorail__return_one__when_the_number_is_zero():
    assert factorial(0) == 1 

# Sad paths

def test_factorial__raise_an_exception__when_the_number_is_a_string():
    with pytest.raises(InvalidArgumentException) as e:
        factorial("cinco")

    assert str(e.value) == "A string argument was passed, integer is required"

def test_factorial__raise_an_exception__when_the_number_is_negative():
    with pytest.raises(InvalidArgumentException) as e:
        factorial(-1)

    assert str(e.value) == "A negative number was passed, integer is required"
