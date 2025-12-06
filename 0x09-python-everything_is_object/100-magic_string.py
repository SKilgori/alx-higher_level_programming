"""Module documentation for 100-magic_string.py."""
#!/usr/bin/python3
def magic_string():
    """magic_string - Function documentation.
    
    Returns:
        Description of the return value.
    """
    magic_string.count = getattr(magic_string, 'count', 0) + 1
    return ", ".join(["BestSchool" for i in range(magic_string.count)])
