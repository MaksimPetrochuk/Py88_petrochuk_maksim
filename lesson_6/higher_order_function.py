def function_1():
    """
    This functions prints its name (function_1)
    """
    print(function_1.__name__)


def function_222():
    """
    This functions prints its name (function_222)
    """
    print(function_222.__name__)


def fy():
    """
    This functions prints its name (bazfoo)
    """
    print(fy.__name__)


def higher_order(x, count=10):
    i = 1
    while i <= count:
        print(i, end=' ')
        x()
        i += 1


higher_order(function_1, 3)
higher_order(function_222, 5)
higher_order(fy, 10)

