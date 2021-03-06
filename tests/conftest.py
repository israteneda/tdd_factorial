from calculator.main import Calculator
from pytest import fixture


class BasicCalculator():
    def sum(self, a, b):
        return a + b


@fixture
def calculator():
    basic_calculator: BasicCalculator = BasicCalculator()
    calculator = Calculator(basic_calculator)
    yield calculator


@fixture
def random_number_generator():
    import random

    def _number_provider():
        return random.choice(range(10))

    yield _number_provider
