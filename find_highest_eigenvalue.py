from typing import Tuple, List

import numpy as np


Matrix = np.array
Vector = np.array

# the eigenvalues for this matrix are 2, 9, and 12
M: Matrix = np.array([[6, -4, 1],
                      [-4, 6, -1],
                      [1, -1, 11]])


def power_method(matrix: Matrix, num_iterations: int) -> Tuple:
    """
        The power method starts with a vector (v_0) containing N=3 number of real numbers
        and iterates through the matrix multiplying v_0 with the matrix, creating v_1.
        Then v_1 is normalized and we recalculate v_0 by dividing v_1 by its normalization.
        As this process is iterated over, we get closer to our eigenvector and its associated
        (highest) eigenvalue of the matrix.
    :param matrix: 3 x 3 matrix
    :param num_iterations: the number of times the power method should iterate
    :return: a tuple (eigenvector, highest_eigenvalue)
    """
    v_0: Vector = np.random.rand(matrix.shape[1])
    v_1_norm: np.linalg.norm = 0
    for x in range(num_iterations):
        v_1: Vector = np.dot(matrix, v_0)

        v_1_norm = np.linalg.norm(v_1)

        v_0 = v_1 / v_1_norm
    return v_0, v_1_norm


def check(test_eigenvector: Vector, matrix: Matrix) -> Vector:
    """
        This function checks to make sure that the eigenvector we calculated
        is correct.
    :param test_eigenvector: The eigenvector associated with the highest eigenvalue
    :param matrix: The matrix we want to test the eigenvector with
    :return:
    """
    checked_vector: Vector = []
    for row in matrix:
        new_val = 0
        for index, val in enumerate(test_eigenvector):
            new_val = new_val + row[index] * val
        checked_vector.append(new_val)
    return checked_vector


def get_eigens(matrix: Matrix) -> Tuple:
    return np.linalg.eig(M)


if __name__ == '__main__':
    highest_eigenvector, highest_eigenvalue = power_method(M, 1000)
    checked = check(highest_eigenvector, M)
    eigens = get_eigens(M)
    eigenvalues = eigens[0]
    eigenvectors = eigens[1]
    print(f'Highest eigenvalue is {highest_eigenvalue} \n'
          f'and the corresponding eigenvector is \n'
          f'{highest_eigenvector}')
    print(check(highest_eigenvector, M))

