from calculator.basic_calculator import BasicCalculator
from calculator.exceptions import InvalidArgumentException
from calculator.constants import NON_NUMBER_INVALID_ARGUMENT, NEGATIVE_INVALID_ARGUMENT


class Calculator():

    def __init__(self, basic_calculator: BasicCalculator):
        pass

    def factorial(self, num: int) -> int:
        """
        Factorial function

        :arg num: Number
        :returns: factorial of num
        """

        if not isinstance(num, int):
            raise InvalidArgumentException(NON_NUMBER_INVALID_ARGUMENT)
        if num < 0:
            raise InvalidArgumentException(NEGATIVE_INVALID_ARGUMENT)

        return num * self.factorial(num - 1) if num else 1

    def fibonacci(top: int) -> int:
        pass
