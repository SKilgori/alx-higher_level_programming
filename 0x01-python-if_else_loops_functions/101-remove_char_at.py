"""Module documentation for 101-remove_char_at.py."""
#!/usr/bin/python3

def remove_char_at(str, n):
    """Create a copy of the string without the character at position n."""
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
