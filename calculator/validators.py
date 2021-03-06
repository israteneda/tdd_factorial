from calculator.constants import NEGATIVE_INVALID_ARGUMENT, NON_NUMBER_INVALID_ARGUMENT
from calculator.exceptions import InvalidArgumentException


def check_invalid_argument(calc_operation):
    def check_invalid_argument_wrapper(self, num):
        if not isinstance(num, int):
            raise InvalidArgumentException(NON_NUMBER_INVALID_ARGUMENT)
        result = calc_operation(self, num)
        return result

    return check_invalid_argument_wrapper


def check_negative_number(calc_operation):
    def check_positive_number_wrapper(self, num):
        if num < 0:
            raise InvalidArgumentException(NEGATIVE_INVALID_ARGUMENT)
        result = calc_operation(self, num)
        return result

    return check_positive_number_wrapper
