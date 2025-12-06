"""Module documentation for 6-print_sorted_dictionary.py."""
#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """print_sorted_dictionary - Function documentation.
    
    Args:
        a_dictionary: Description of a_dictionary.
    
    Returns:
        Description of the return value.
    """
    for keys in sorted(a_dictionary.keys()):
        print('{}: {}'. format(keys, a_dictionary[keys]))
