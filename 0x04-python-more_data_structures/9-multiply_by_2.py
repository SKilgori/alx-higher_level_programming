"""Module documentation for 9-multiply_by_2.py."""
#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """multiply_by_2 - Function documentation.
    
    Args:
        a_dictionary: Description of a_dictionary.
    
    Returns:
        Description of the return value.
    """
    return {key: val * 2 for key, val in a_dictionary.items()}
