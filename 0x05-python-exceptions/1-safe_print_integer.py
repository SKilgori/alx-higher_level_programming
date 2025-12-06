"""Module documentation for 1-safe_print_integer.py."""
#!/usr/bin/python3
def safe_print_integer(value):
    """safe_print_integer - Function documentation.
    
    Args:
        value: Description of value.
    
    Returns:
        Description of the return value.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
