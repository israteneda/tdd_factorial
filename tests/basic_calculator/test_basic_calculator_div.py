import pytest


def test_div__the_division_returns_a_decimal_number__when_the_dividend_is_not_a_multiple_of_the_divisor(
        basic_calculator):
    assert isinstance(basic_calculator.div(11, 4), float)


def test_div__the_division_returns_an_integer_number__when_the_divided_is_a_multiple_of_the_divisor(basic_calculator):
    assert float(basic_calculator.div(8, 4)).is_integer()


def test_div__the_division_raise_an_exception__when_the_divisor_is_zero(basic_calculator):
    with pytest.raises(ZeroDivisionError) as e:
        basic_calculator.div(5, 0)

    assert str(e.value) == 'division by zero'


def test_div__the_dividend_and_the_quotient_are_the_same__when_the_divisor_is_one(basic_calculator):
    assert basic_calculator.div(20, 1) == 20
