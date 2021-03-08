from calculator.basic_calculator import BasicCalculator
from calculator.validators import check_negative_number, check_invalid_argument
from typing import List


class Calculator:

    def __init__(self, basic_calculator: BasicCalculator):
        self.basic_calculator = basic_calculator

    @check_invalid_argument
    @check_negative_number
    def factorial(self, num: int) -> int:
        """
        Returns the factorial of a num

        Parameter:
            num (int): number to calculate the factorial

        Returns:
           res (int): factorial of a num
        """

        res = num * self.factorial(num - 1) if num else 1
        return res

    @check_invalid_argument
    @check_negative_number
    def fibonacci(self, top: int) -> List[int]:
        """
        Returns the fibonacci sequence

        Parameter:
            top (int): top limit
        Returns:
            fibonacci_sequence (list[int]): fibonacci sequence
        """

        fibonacci_sequence: List[int] = [0, 1]
        num: int = 1
        previous_num: int = 0

        while num <= top:
            tmp: int = num
            num = self.basic_calculator.sum(previous_num, num)
            fibonacci_sequence.append(num)
            previous_num = tmp

        return fibonacci_sequence[:-1]
