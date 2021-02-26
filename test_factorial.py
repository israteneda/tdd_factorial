from factorial import factorial
from factorial import InvalidArgument
import pytest

# Happy paths

# def test_factorial__return_the_factorial__when_the_number_is_positive_v1():
#    assert factorial(2) == 2

def test_factorial__return_the_number_one__when_the_number_is_one_v2():
    assert factorial(1) == 1

def test_factorail__return_the_number_six__when_the_number_is_three():
    assert factorial(3) == 6


# Bad paths

def test_factorial__raise_an_exception__when_the_number_is_a_string():
    with pytest.raises(InvalidArgument) as e:
        factorial("cinco")

    assert str(e.value) == "An incorrect argument was passed"
