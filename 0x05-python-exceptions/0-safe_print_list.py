"""Module documentation for 0-safe_print_list.py."""
#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list.
    
    Args:
        my_list (list): The list to print elements from.
        x (int): The maximum number of elements to print.
    
    Returns:
        The number of elements actually printed.
    """
    total = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            total += 1
        except IndexError as e:
            break
    print()
    return (total)
