from calculator.main import Calculator
from calculator.basic_calculator import BasicCalculator
from pytest import fixture


@fixture
def basic_calculator():
    basic_calculator = BasicCalculator()
    yield basic_calculator


@fixture
def calculator():
    calculator = Calculator(basic_calculator=None)
    yield calculator


@fixture
def random_number_generator():
    import random

    def _number_provider():
        return random.choice(range(10))

    yield _number_provider
