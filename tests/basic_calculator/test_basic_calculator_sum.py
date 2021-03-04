def test_sum__the_sum_returns_a_positive_number__when_numbers_are_positive(random_number_generator, basic_calculator):
    first_number = random_number_generator()
    second_number = random_number_generator()
    result = basic_calculator.sum(first_number, second_number)
    assert result == first_number + second_number
