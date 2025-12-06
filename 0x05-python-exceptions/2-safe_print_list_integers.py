"""Module documentation for 2-safe_print_list_integers.py."""
#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """safe_print_list_integers - Function documentation.
    
    Args:
        my_list: Description of my_list.
        x: Description of x.
    
    Returns:
        Description of the return value.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print()
    return (count)
