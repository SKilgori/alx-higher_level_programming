"""Module documentation for 8-uppercase.py."""
#!/usr/bin/python3
def uppercase(str):
    """uppercase - Function documentation.
    
    Args:
        str: Description of str.
    
    Returns:
        Description of the return value.
    """
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
            print("{}".format(i), end="")
            print()
