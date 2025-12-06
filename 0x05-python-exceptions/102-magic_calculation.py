"""Module documentation for 102-magic_calculation.py."""
#!/usr/bin/python3
def magic_calculation(a, b):
    """magic_calculation - Function documentation.
    
    Args:
        a: Description of a.
        b: Description of b.
    
    Returns:
        Description of the return value.
    """
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                result += (a ** b) / i
        except Exception:
            result = b + a
            break
    return (result)
