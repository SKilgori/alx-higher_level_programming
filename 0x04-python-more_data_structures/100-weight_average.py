"""Module documentation for 100-weight_average.py."""
#!/usr/bin/python3
def weight_average(my_list=[]):
    """weight_average - Function documentation.
    
    Args:
        my_list: Description of my_list.
    
    Returns:
        Description of the return value.
    """
    if my_list and len(my_list):
        num = 0
        denom = 0
        for tup in my_list:
            num += (tup[0] * tup[1])
            denom += (tup[1])
        return (num/denom)
    return 0
