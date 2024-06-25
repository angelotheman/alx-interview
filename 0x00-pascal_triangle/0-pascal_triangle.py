#!/usr/bin/python3
"""
Solve the pascal triangle question
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers of the triangle with input size (N)
    """
    if n <= 0:
        return []

    triangle = []

    for row in range(n):
        current_row = []

        for j in range(row + 1):
            if j == 0 or j == row:
                current_row.append(1)
            else:
                current_row.append(
                        triangle[row - 1][j - 1] + triangle[row - 1][j]
                    )

        triangle.append(current_row)

    return triangle
