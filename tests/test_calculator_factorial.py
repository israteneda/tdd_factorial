from calculator.exceptions import InvalidArgumentException
from tests.data.constants import NON_NUMBER_INVALID_ARGUMENT, NEGATIVE_INVALID_ARGUMENT
import pytest

def test_fibonacci__check_if_fibonacci_function_exists__when_the_program_runs(mocker, calculator):
    fibonacci = mocker.spy(calculator, 'fibonacci')
    calculator.fibonacci()
    fibonacci.assert_called()

# Happy paths


def factorial__return_the_factorial_of_the_number__when_the_number_is_positive(calculator):

    assert calculator.factorial(1) == 1
    assert calculator.factorial(2) == 2
    assert calculator.factorial(3) == 6
    assert calculator.factorial(4) == 24
    assert calculator.factorial(10) == 3628800


def test_factorail__return_a_positive_number__when_the_number_is_positive(random_number_generator, calculator):
    number = random_number_generator()

    assert calculator.factorial(number) > 0 


def test_factorail__return_one__when_the_number_is_zero(calculator):

    assert calculator.factorial(0) == 1 

# Edge cases 


def test_factorial__raise_an_exception__when_the_number_is_a_string(calculator):
    with pytest.raises(InvalidArgumentException) as e:
        calculator.factorial("cinco")

    assert str(e.value) == NON_NUMBER_INVALID_ARGUMENT


def test_factorial__raise_an_exception__when_the_number_is_float(calculator):
    with pytest.raises(InvalidArgumentException) as e:
        calculator.factorial(5.5)

    assert str(e.value) == NON_NUMBER_INVALID_ARGUMENT


def test_factorial__raise_an_exception__when_the_number_is_negative(calculator):
    with pytest.raises(InvalidArgumentException) as e:
        calculator.factorial(-1)

    assert str(e.value) == NEGATIVE_INVALID_ARGUMENT