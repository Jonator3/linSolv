import numpy as np

example_a = np.array([
    [9,    6, -3,  3,],
    [6,   -6, 12, -6,],
    [-3, 1.5, -3,  0,],
], dtype=np.float64)

example_b = np.array([
    [4, 7, -12, -8,  2],
    [5, 8, -9,  -1,  0],
    [6, 9, -24, -9, -2],
], dtype=np.float64)


def sort_matrix_rows(a: np.ndarray) -> np.ndarray:
    a = a.copy()

    if a[0, 0] == 0:
        row_without_leading_zero = 0
        for row in range(1, a.shape[0]):
            if a[row, 0] != 0:
                row_without_leading_zero = row

        a[0, :], a[row_without_leading_zero, :] = a[row_without_leading_zero, :], a[0, :]

    return a


def triangle_matrix(a: np.ndarray) -> np.ndarray:
    a = a.copy()

    for column in range(a.shape[0]):
        if a[column, column] != 0:
            for row in range(column + 1, a.shape[0]):
                a[row, :] -= (a[row, column] / a[column, column]) * a[column, :]
    return a


def main_diagonal_matrix(a: np.ndarray) -> np.ndarray:
    a = triangle_matrix(a).copy()

    for column in range(a.shape[0]-1, -1, -1):
        if a[column, column] != 0:
            for row in range(column - 1, -1, -1):
                a[row, :] -= (a[row, column] / a[column, column]) * a[column, :]
    return a


def normalize_diagonal(a: np.ndarray) -> np.ndarray:
    a = a.copy()

    for i in range(a.shape[0]):
        a[i, :] /= a[i, i]

    return a


def determinant(a: np.ndarray) -> float:
    a = main_diagonal_matrix(a)

    return np.prod([a[i, i] for i in range(a.shape[0])])


def solve_lse(a: np.ndarray) -> np.ndarray:
    a = main_diagonal_matrix(a).copy()

    x = np.zeros((a.shape[0],))
    for i in range(x.shape[0]):
        x[i] = (a[i, a.shape[1]-1]) / a[i, i]  # TODO: ¯\_(ツ)_/¯

    return np.array([x]).T


if __name__ == '__main__':
    print("Matrix A:")
    print(example_a)
    print("Diagonal form:")
    print(example_a_diagonalized := main_diagonal_matrix(example_a))
    print("Normalized diagonal:")
    print(normalize_diagonal(example_a_diagonalized))
    print("Solution vector:")
    print(solve_lse(example_a))
    print("Determinant:", determinant(example_a))

    print("Matrix B:")
    print(example_b)
    print("Diagonal form:")
    print(example_b_diagonalized := main_diagonal_matrix(example_b))
    print("Normalized diagonal:")
    print(normalize_diagonal(example_b_diagonalized))
