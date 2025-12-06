"""Module documentation for 101-safe_function.py."""
#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """safe_function - Function documentation.
    
    Args:
        fct: Description of fct.
    
    Returns:
        Description of the return value.
    """
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
