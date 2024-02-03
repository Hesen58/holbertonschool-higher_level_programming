#!/usr/bin/python3
def safe_print_division(a, b):
    zor = None
    try:
        zor = a / b
    except (TypeError, ValueError, ZeroDivisionError):
        return None
    finally:
        print("Inside result: {}".format(zor))
    return zor
