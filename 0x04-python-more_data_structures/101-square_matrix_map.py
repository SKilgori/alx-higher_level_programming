"""Module documentation for 101-square_matrix_map.py."""
#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    """square_matrix_map - Function documentation.
    
    Args:
        matrix: Description of matrix.
    
    Returns:
        Description of the return value.
    """
    return list(map((lambda row: list(map((lambda x: x * x), row))), matrix))
