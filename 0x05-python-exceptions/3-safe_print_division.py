#!/usr/bin/python3
"""Module that safely divides two numbers.

Handles division by zero and type errors gracefully.
"""


def safe_print_division(a, b):
    """Divides two numbers and handles exceptions.

    Args:
        a (int/float): The numerator.
        b (int/float): The denominator.

    Returns:
        float or None: The result of the division, or None if an error occurred.
    """
    div = None
    try:
        div = a / b
    except (TypeError, ZeroDivisionError) as e:
        # The function is designed to return None on error, so no further action is needed here.
        pass
    finally:
        print("Inside result: {}".format(div))
    return div
