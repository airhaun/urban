from math import inf


def true_divide(first, second):
    try:
        k = first / second
        print(k)
    except ZeroDivisionError:
        return inf

