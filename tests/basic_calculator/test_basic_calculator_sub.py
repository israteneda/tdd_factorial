def test_sub__the_subtraction_returns_a_positive_number__when_the_first_number_is_bigger_than_second_number(
        basic_calculator):
    assert basic_calculator.sub(6, 5) > 0


def test_sub__the_subtraction_returns_a_negative_number__when_the_first_number_is_lower_than_second_number(
        basic_calculator):
    assert basic_calculator.sub(5, 6) < 0


def test_sub_the_subtraction_returns_zero__when_the_numbers_are_same(basic_calculator):
    assert basic_calculator.sub(6, 6) == 0

