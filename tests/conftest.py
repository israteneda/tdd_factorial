from calculator.main import Calculator
from calculator.basic_calculator import BasicCalculator
import pytest


@pytest.fixture
def basic_calculator():
    basic_calculator = BasicCalculator()
    yield basic_calculator


@pytest.fixture
def calculator():
    calculator = Calculator(basic_calculator=None)
    yield calculator


@pytest.fixture
def random_number_generator():
    import random

    def _number_provider():
        return random.choice(range(10))

    yield _number_provider
