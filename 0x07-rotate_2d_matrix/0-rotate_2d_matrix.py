#!/usr/bin/python3
"""Matrix"""


def rotate_2d_matrix(matrix):
    """Rotates the matix 
    """
    replica = matrix[:]

    for i in range(len(matrix)):
        """retract column from replica"""
        col = [row[i] for row in replica]
        matrix[i] = col[::-1]
