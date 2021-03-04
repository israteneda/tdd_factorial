def test_multiply__the_product_of_the_multiplication_is_the_same_of_the_one_factor__when_on_of_the_factor_is_one(
        basic_calculator):
    assert basic_calculator.multiply(5, 1) == 5


def test_multiply__the_product_of_the_multiplication_is_positive__when_the_factors_are_positive(basic_calculator):
    assert basic_calculator.multiply(1, 2) > -0


def test_multiply__the_product_of_the_multipication_is_zero__when_one_of_the_factors_is_zero(basic_calculator):
    assert basic_calculator.multiply(1, 0) == 0
