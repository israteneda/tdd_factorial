from tests.data.constants import NEGATIVE_INVALID_ARGUMENT
from calculator.exceptions import InvalidArgumentException
import pytest


def test_sum__the_sum_returns_a_positive_number__when_numbers_are_positive(random_number_generator, basic_calculator):
    first_number = random_number_generator()
    second_number = random_number_generator()
    result = basic_calculator.sum(first_number, second_number)
    assert result == first_number + second_number


def test_sum__raise_an_exception__when_the_number_is_negative(basic_calculator):
    with pytest.raises(InvalidArgumentException) as e:
        basic_calculator.sum(-1, 2)

    assert str(e.value) == NEGATIVE_INVALID_ARGUMENT


def test_sub__the_subtraction_returns_a_positive_number__when_the_first_number_is_bigger_than_second_number(
        basic_calculator):
    assert basic_calculator.sub(6, 5) > 0


def test_sub__the_subtraction_returns_a_negative_number__when_the_first_number_is_lower_than_second_number(
        basic_calculator):
    assert basic_calculator.sub(5, 6) < 0


def test_sub_the_subtraction_returns_zero__when_the_numbers_are_same(basic_calculator):
    assert basic_calculator.sub(6, 6) == 0


def test_sub__raise_an_exception__when_the_number_is_negative(basic_calculator):
    with pytest.raises(InvalidArgumentException) as e:
        basic_calculator.sub(-1, 2)

    assert str(e.value) == NEGATIVE_INVALID_ARGUMENT


def test_div__the_division_returns_a_decimal_number__when_the_dividend_is_not_a_multiple_of_the_divisor(
        basic_calculator):
    assert isinstance(basic_calculator.div(11, 4), float)


def test_div__the_division_returns_an_integer_number__when_the_divided_is_a_multiple_of_the_divisor(basic_calculator):
    assert float(basic_calculator.div(8, 4)).is_integer()


def test_div__the_division_raise_an_exception__when_the_divisor_is_zero(basic_calculator):
    with pytest.raises(ZeroDivisionError) as e:
        basic_calculator.div(5, 0)

    assert str(e.value) == 'division by zero'


def test_div__raise_an_exception__when_the_number_is_negative(basic_calculator):
    with pytest.raises(InvalidArgumentException) as e:
        basic_calculator.div(-1, 2)

    assert str(e.value) == NEGATIVE_INVALID_ARGUMENT


def test_div__the_dividend_and_the_quotient_are_the_same__when_the_divisor_is_one(basic_calculator):
    assert basic_calculator.div(20, 1) == 20


def test_multiply__the_product_of_the_multiplication_is_the_same_of_the_one_factor__when_on_of_the_factor_is_one(
        basic_calculator):
    assert basic_calculator.multiply(5, 1) == 5


def test_multiply__the_product_of_the_multiplication_is_positive__when_the_factors_are_positive(basic_calculator):
    assert basic_calculator.multiply(1, 2) > -0


def test_multiply__the_product_of_the_multipication_is_zero__when_one_of_the_factors_is_zero(basic_calculator):
    assert basic_calculator.multiply(1, 0) == 0


def test_multiply__raise_an_exception__when_the_number_is_negative(basic_calculator):
    with pytest.raises(InvalidArgumentException) as e:
        basic_calculator.multiply(-1, 2)

    assert str(e.value) == NEGATIVE_INVALID_ARGUMENT

