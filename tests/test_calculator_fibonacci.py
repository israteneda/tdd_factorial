import pytest

from calculator.exceptions import InvalidArgumentException
from tests.data.constants import NEGATIVE_INVALID_ARGUMENT, NON_NUMBER_INVALID_ARGUMENT


def test_fibonacci__check_if_fibonacci_function_exists__when_the_program_runs(mocker, calculator):
    fibonacci = mocker.spy(calculator, 'fibonacci')
    calculator.fibonacci(1)
    fibonacci.assert_called_with(1)


def test_fibonacci__raise_an_exception__when_the_number_is_negative(calculator):
    with pytest.raises(InvalidArgumentException) as e:
        calculator.fibonacci(-1)

    assert str(e.value) == NEGATIVE_INVALID_ARGUMENT


def test_fibonacci__raise_an_exception__when_the_number_is_not_an_integer(calculator):
    with pytest.raises(InvalidArgumentException) as e:
        calculator.fibonacci("cuatro")

    assert str(e.value) == NON_NUMBER_INVALID_ARGUMENT
