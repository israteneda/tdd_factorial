class InvalidArgumentException(Exception):
    pass


def factorial_v1(num):
    if not isinstance(num, int):
        raise InvalidArgumentException("A string argument was passed, integer is required")
    if num < 0:
        raise InvalidArgumentException("A negative number was passed, integer is required")
    if num == 0:
        return 1
    if num == 1:
        return 1
    else:
        return num * factorial_v1(num - 1)

def factorial_v2(num):
    if not isinstance(num, int):
        raise InvalidArgumentException("A string argument was passed, integer is required")
    if num < 0:
        raise InvalidArgumentException("A negative number was passed, integer is required")
    if num == 0:
        return 1
    else:
        return num * factorial_v2(num - 1)

def factorial(num):
    if not isinstance(num, int):
        raise InvalidArgumentException("A string argument was passed, integer is required")
    if num < 0:
        raise InvalidArgumentException("A negative number was passed, integer is required")
    
    return num * factorial(num - 1) if num else 1


