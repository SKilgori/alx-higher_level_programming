"""Module documentation for 11-multiply_list_map.py."""
#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """multiply_list_map - Function documentation.
    
    Args:
        my_list: Description of my_list.
        number: Description of number.
    
    Returns:
        Description of the return value.
    """
    return list(map(lambda x: x * number, my_list))
