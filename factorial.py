from constants import STRING_INVALID_ARGUMENT, NEGATIVE_INVALID_ARGUMENT


class InvalidArgumentException(Exception):
    pass


def factorial_v1(num):
    if not isinstance(num, int):
        raise InvalidArgumentException(STRING_INVALID_ARGUMENT)
    if num < 0:
        raise InvalidArgumentException(NEGATIVE_INVALID_ARGUMENT)
    if num == 0:
        return 1
    if num == 1:
        return 1
    else:
        return num * factorial_v1(num - 1)

def factorial_v2(num):
    if not isinstance(num, int):
        raise InvalidArgumentException(STRING_INVALID_ARGUMENT)
    if num < 0:
        raise InvalidArgumentException(NEGATIVE_INVALID_ARGUMENT)
    if num == 0:
        return 1
    else:
        return num * factorial_v2(num - 1)

def factorial(num):
    """
    Factorial function

    :arg num: Number
    :returns: factorial of num
    """

    if not isinstance(num, int):
        raise InvalidArgumentException(STRING_INVALID_ARGUMENT)
    if num < 0:
        raise InvalidArgumentException(NEGATIVE_INVALID_ARGUMENT)

    return num * factorial(num - 1) if num else 1


