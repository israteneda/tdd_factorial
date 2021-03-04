from calculator.basic_calculator import BasicCalculator
from calculator.validators import check_negative_number, check_invalid_argument


class Calculator():

    def __init__(self, basic_calculator: BasicCalculator):
        pass

    @check_invalid_argument
    @check_negative_number
    def factorial(self, num: int) -> int:
        """
        Returns the factorial of a num

        Parameter:
            num (int): number to calculate the factorial

        Returns:
           factorial (int): factorial of a num
        """
        factorial = num * self.factorial(num - 1) if num else 1
        return factorial

    @check_invalid_argument
    @check_negative_number
    def fibonacci(self, top: int) -> int:
        """
        Returns the fibonacci sequence

        Parameter:
            top (int): top limit
        Returns:
            fibonacci_sequence (list[int]): fibonacci sequence
        """
        pass
