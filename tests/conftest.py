from calculator.main import Calculator
from pytest import fixture


def mock_sum(a, b):
    return a + b


@fixture
def calculator(mocker):
    mock_basic_calculator = mocker.Mock()
    mock_basic_calculator.sum = mocker.Mock(side_effect=mock_sum)
    calculator = Calculator(mock_basic_calculator)
    yield calculator


@fixture
def random_number_generator():
    import random

    def _number_provider():
        return random.choice(range(10))

    yield _number_provider
