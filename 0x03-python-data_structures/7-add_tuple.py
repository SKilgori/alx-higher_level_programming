"""Module documentation for 7-add_tuple.py."""
#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """add_tuple - Function documentation.
    
    Args:
        tuple_a: Description of tuple_a.
        tuple_b: Description of tuple_b.
    
    Returns:
        Description of the return value.
    """
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuple_a = 0, 0
        else:
            tuple_a = tuple_a[0], 0

    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0

    added_tuple = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return added_tuple
