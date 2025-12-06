"""Module documentation for 6-print_matrix_integer.py."""
#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """print_matrix_integer - Function documentation.
    
    Args:
        matrix: Description of matrix.
    
    Returns:
        Description of the return value.
    """
    for row in matrix:
        for column in row:
            if column == row[-1]:
                print('{:d}'.format(column), end='')
            else:
                print('{:d}'.format(column), end=' ')
        print()
