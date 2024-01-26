import numpy as np


def laplace_det(mat):
    if mat.shape[0] == 1:
        return mat[0, 0]

    return sum([(((-1) ** k) * mat[0, k] * laplace_det(stroke_mat(mat, 0, k))) for k in range(mat.shape[0])])


def stroke_mat(mat, k, l):
    return np.delete(np.delete(mat, k, 0), l, 1)


test_mat = np.array([
    [0, 2, 3, ],
    [4, 5, 6, ],
    [7, 8, 9, ],
], dtype=np.float64)

test_mat2 = np.array([
    [0, 1, 2, ],
    [3, 2, 1, ],
    [1, 1, 0, ],
], dtype=np.float64)

print(laplace_det(test_mat2))
