from factorial import factorial
from factorial import InvalidArgumentException
from constants import NON_NUMBER_INVALID_ARGUMENT, NEGATIVE_INVALID_ARGUMENT
import pytest

# Happy paths

def test_factorial__return_the_factorial_of_the_number__when_the_number_is_positive():
    
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(10) == 3628800

def test_factorail__return_a_positive_number__when_the_number_is_positive(random_number_generator):
    number = random_number_generator()

    assert factorial(number) > 0 

def test_factorail__return_one__when_the_number_is_zero():

    assert factorial(0) == 1 

# Sad paths

def test_factorial__raise_an_exception__when_the_number_is_a_string():
    with pytest.raises(InvalidArgumentException) as e:
        factorial("cinco")

    assert str(e.value) == NON_NUMBER_INVALID_ARGUMENT

def test_factorial__raise_an_exception__when_the_number_is_negative():
    with pytest.raises(InvalidArgumentException) as e:
        factorial(-1)

    assert str(e.value) == NEGATIVE_INVALID_ARGUMENT
