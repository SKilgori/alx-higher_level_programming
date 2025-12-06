"""Module documentation for 8-simple_delete.py."""
#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """simple_delete - Function documentation.
    
    Args:
        a_dictionary: Description of a_dictionary.
        key: Description of key.
    
    Returns:
        Description of the return value.
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
