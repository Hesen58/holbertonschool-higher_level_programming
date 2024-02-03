#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        zor = a / b
    except (TypeError, ValueError, ZeroDivisionError, UnboundLocalError):
        return None
    finally:
        print("Inside result: {}".format(zor))
    return zor
