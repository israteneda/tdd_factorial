class InvalidArgument(Exception):
    pass


def factorial(num):
    if not isinstance(num, int):
        raise InvalidArgument("An incorrect argument was passed")
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)
