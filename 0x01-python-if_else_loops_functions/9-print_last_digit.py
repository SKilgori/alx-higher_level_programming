"""Module documentation for 9-print_last_digit.py."""
#!/usr/bin/python3

def print_last_digit(number):
    """print_last_digit - Function documentation.
    
    Args:
        number: Description of number.
    
    Returns:
        Description of the return value.
    """
    print(abs(number) % 10, end="")
    return (abs(number) % 10)
