from calculator.constants import NEGATIVE_INVALID_ARGUMENT
from calculator.exceptions import InvalidArgumentException


class BasicCalculator():

    def _validator(basic_calc_operation):
        def validator_wrapper(self, x, y):
            if x < 0 or y < 0:
                raise InvalidArgumentException(NEGATIVE_INVALID_ARGUMENT)
            result = basic_calc_operation(self, x, y)
            return result

        return validator_wrapper

    @_validator
    def sum(self, first_number: int, second_number: int) -> int:
        return first_number + second_number

    @_validator
    def sub(self, first_number: int, second_number: int) -> int:
        return first_number - second_number

    @_validator
    def div(self, first_number: int, second_number: int) -> float:
        return first_number / second_number

    @_validator
    def multiply(self, first_number: int, second_number: int) -> int:
        return first_number * second_number
