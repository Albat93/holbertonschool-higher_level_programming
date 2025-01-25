#!/usr/bin/python3
"""
This module defines a function `matrix_divided` which divides
all elements of a matrix by a given divisor.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix (list of lists of int/float): Matrix to be divided.
        div (int/float): The divisor.

    Returns:
        list: A new matrix with all elements divided by div, rounded to 2
        decimals.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   if rows are not of the same size, or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    if not all(all(isinstance(elem, (int, float)) for elem in row)
               for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
