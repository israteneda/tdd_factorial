from typing import List
import pytest

from calculator.exceptions import InvalidArgumentException
from calculator.main import Calculator
from tests.data.constants import NEGATIVE_INVALID_ARGUMENT, NON_NUMBER_INVALID_ARGUMENT

# Happy path
from tests.data.fibonacci import fibonacci_sequence


def test_fibonacci__check_if_fibonacci_function_exists__when_the_program_runs(mocker):
    mock_basic_calculator = mocker.Mock()
    mock_basic_calculator.sum = mocker.Mock(side_effect=[1, 2])
    calculator: Calculator = Calculator(mock_basic_calculator)
    fibonacci = mocker.spy(calculator, 'fibonacci')

    calculator.fibonacci(1)

    fibonacci.assert_called_with(1)


def test_fibonacci__returns_a_list_with_zero__when_the_number_is_zero(mocker):
    mock_basic_calculator = mocker.Mock()
    mock_basic_calculator.sum = mocker.Mock(side_effect=[1])
    calculator = Calculator(mock_basic_calculator)

    result: int = calculator.fibonacci(0)

    assert result == [0]


def test_fibonacci__return_the_list_zero_one_one__when_the_number_is_one(mocker):
    mock_basic_calculator = mocker.Mock()
    mock_basic_calculator.sum = mocker.Mock(side_effect=[1, 2])
    calculator = Calculator(mock_basic_calculator)

    result: int = calculator.fibonacci(1)

    assert result == [0, 1, 1]


def test_fibonacci_return_the_list_zero_one_one_two__when_the_number_is_two(mocker):
    mock_basic_calculator = mocker.Mock()
    mock_basic_calculator.sum = mocker.Mock(side_effect=[1, 2, 3])
    calculator = Calculator(mock_basic_calculator)

    result: int = calculator.fibonacci(2)

    assert result == [0, 1, 1, 2]


def test_fibonacci_return_the_fibonacci_sequence__when_the_number_is_four(mocker):
    mock_basic_calculator = mocker.Mock()
    mock_basic_calculator.sum = mocker.Mock(side_effect=[1, 2, 3, 5])
    calculator = Calculator(mock_basic_calculator)

    result: int = calculator.fibonacci(4)

    assert result == [0, 1, 1, 2, 3]


def test_fibonacci_return_the_fibonacci_sequence__when_the_number_is_five(mocker):
    mock_basic_calculator = mocker.Mock()
    mock_basic_calculator.sum = mocker.Mock(side_effect=[1, 2, 3, 5, 8])
    calculator = Calculator(mock_basic_calculator)

    result: int = calculator.fibonacci(5)

    assert result == [0, 1, 1, 2, 3, 5]


def test_fibonacci_return_the_fibonacci_sequence__when_the_number_is_nine(mocker):
    mock_basic_calculator = mocker.Mock()
    mock_basic_calculator.sum = mocker.Mock(side_effect=[1, 2, 3, 5, 8, 13])
    calculator = Calculator(mock_basic_calculator)

    result: int = calculator.fibonacci(9)

    assert result == [0, 1, 1, 2, 3, 5, 8]


def test_fibonacci_return_the_fibonacci_sequence__when_the_number_is_one_thousand(mocker):
    mock_basic_calculator = mocker.Mock()
    mock_basic_calculator.sum = mocker.Mock(
        side_effect=[1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
    )
    calculator = Calculator(mock_basic_calculator)

    result: int = calculator.fibonacci(1000)

    assert result == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]


# Sad paths


def test_fibonacci__raise_an_exception__when_the_number_is_negative():
    calculator: Calculator = Calculator(None)

    with pytest.raises(InvalidArgumentException) as e:
        calculator.fibonacci(-1)

    assert str(e.value) == NEGATIVE_INVALID_ARGUMENT


def test_fibonacci__raise_an_exception__when_the_number_is_not_an_integer():
    calculator: Calculator = Calculator(None)

    with pytest.raises(InvalidArgumentException) as e:
        calculator.fibonacci("cuatro")

    assert str(e.value) == NON_NUMBER_INVALID_ARGUMENT


# Edge cases

def test_fibonacci_return_the_fibonacci_sequence__when_the_number_is_5000000000000(mocker):
    mock_basic_calculator = mocker.Mock()
    mock_basic_calculator.sum = mocker.Mock(side_effect=fibonacci_sequence)
    calculator = Calculator(mock_basic_calculator)
    expected_list: List[int] = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181,
                                6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040,
                                1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986,
                                102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903,
                                2971215073, 4807526976, 7778742049, 12586269025, 20365011074, 32951280099, 53316291173,
                                86267571272, 139583862445, 225851433717, 365435296162, 591286729879, 956722026041,
                                1548008755920, 2504730781961, 4052739537881]

    result: List[int] = calculator.fibonacci(5000000000000)

    assert result == expected_list
