import math
from typing import List


def mat_(mat, n, k):
    out = []
    for ri in range(len(mat)):
        if ri != n:
            out.append([mat[ri][ci] for ci in range(len(mat)) if ci != k])
    return out


def det(mat: List[List[float]]) -> float:
    n = len(mat[0])
    if len(mat) != n:
        raise ValueError('Matrix must be square Matrix')
    if n == 1:
        return mat[0][0]

    return sum([((-1)**k) * mat[0][k] * det(mat_(mat, 0, k)) for k in range(n)])


def ggT(a: int, b: int) -> int:
    if a < b:
        return ggT(b, a)
    q = math.floor(a/b)
    c = (-q)*b+a
    if c == 0:
        return b
    else:
        return ggT(b, c)


if __name__ == '__main__':
    import linSolv
    import random

    print("TEST det:")
    print(det([[1, 0], [0, 1]]) == 1)

    for i in range(5):
        mat = [
            [random.random(), random.random(), random.random()],
            [random.random(), random.random(), random.random()],
            [random.random(), random.random(), random.random()],
        ]
        print(abs(linSolv.det(mat) - det(mat)) < 0.0001)

    print("\nTEST ggT:")
    def brut_ggt(a: int, b: int) -> int:
        if a < b:
            return brut_ggt(b, a)
        for i in range(b):
            c = b-i
            if a % c == 0 and b % c == 0:
                return c

    for i in range(5):
        a = random.randint(100, 10**5)
        b = random.randint(100, 10**5)

        print(ggT(a, b) == brut_ggt(a, b))
