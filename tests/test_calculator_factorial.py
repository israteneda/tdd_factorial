from calculator.exceptions import InvalidArgumentException
from calculator.main import Calculator
from tests.data.constants import NON_NUMBER_INVALID_ARGUMENT, NEGATIVE_INVALID_ARGUMENT
import pytest


# Happy paths


def test_factorial__return_the_factorial_of_the_number__when_the_number_is_positive(mocker):
    mock_basic_calculator = mocker.Mock()
    calculator: Calculator = Calculator(mock_basic_calculator)

    assert calculator.factorial(1) == 1
    assert calculator.factorial(2) == 2
    assert calculator.factorial(3) == 6
    assert calculator.factorial(4) == 24
    assert calculator.factorial(10) == 3628800


def test_factorial__return_a_positive_number__when_the_number_is_positive(
        mocker,
        random_number_generator
    ):
    mock_basic_calculator = mocker.Mock()
    calculator: Calculator = Calculator(mock_basic_calculator)
    number: int = random_number_generator()

    assert calculator.factorial(number) > 0


def test_factorial__return_one__when_the_number_is_zero(mocker):
    mock_basic_calculator = mocker.Mock()
    calculator: Calculator = Calculator(mock_basic_calculator)

    assert calculator.factorial(0) == 1


# Sad paths


def test_factorial__raise_an_exception__when_the_number_is_a_string(mocker):
    mock_basic_calculator = mocker.Mock()
    calculator: Calculator = Calculator(mock_basic_calculator)

    with pytest.raises(InvalidArgumentException) as e:
        calculator.factorial("cinco")

    assert str(e.value) == NON_NUMBER_INVALID_ARGUMENT


def test_factorial__raise_an_exception__when_the_number_is_float(mocker):
    mock_basic_calculator = mocker.Mock()
    calculator: Calculator = Calculator(mock_basic_calculator)

    with pytest.raises(InvalidArgumentException) as e:
        calculator.factorial(5.5)

    assert str(e.value) == NON_NUMBER_INVALID_ARGUMENT


def test_factorial__raise_an_exception__when_the_number_is_negative(mocker):
    mock_basic_calculator = mocker.Mock()
    calculator: Calculator = Calculator(mock_basic_calculator)

    with pytest.raises(InvalidArgumentException) as e:
        calculator.factorial(-1)

    assert str(e.value) == NEGATIVE_INVALID_ARGUMENT
