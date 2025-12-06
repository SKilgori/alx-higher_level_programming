"""Module documentation for 0-square_matrix_simple.py."""
#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """square_matrix_simple - Function documentation.
    
    Args:
        matrix: Description of matrix.
    
    Returns:
        Description of the return value.
    """
    return [list(map(lambda x: x ** 2, row)) for row in matrix]
