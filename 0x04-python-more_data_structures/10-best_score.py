"""Module documentation for 10-best_score.py."""
#!/usr/bin/python3
def best_score(a_dictionary):
    """best_score - Function documentation.
    
    Args:
        a_dictionary: Description of a_dictionary.
    
    Returns:
        Description of the return value.
    """
    return max(a_dictionary, key=a_dictionary.get) if a_dictionary else None
