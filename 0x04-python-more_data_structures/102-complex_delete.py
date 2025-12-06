"""Module documentation for 102-complex_delete.py."""
#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """complex_delete - Function documentation.
    
    Args:
        a_dictionary: Description of a_dictionary.
        value: Description of value.
    
    Returns:
        Description of the return value.
    """
    keys_to_del = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            keys_to_del.append(key)
    for key in keys_to_del:
        del a_dictionary[key]
    return a_dictionary
