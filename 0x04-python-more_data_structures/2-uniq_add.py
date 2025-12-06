"""Module documentation for 2-uniq_add.py."""
#!/usr/bin/python3
def uniq_add(my_list=[]):
    """uniq_add - Function documentation.
    
    Args:
        my_list: Description of my_list.
    
    Returns:
        Description of the return value.
    """
    number = 0
    for element in set(my_list):
        number += element
    return number
