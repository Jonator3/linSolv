import math
from typing import List, Tuple


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


def ggT_mxy(a: int,b: int,) -> Tuple[int, int, int]:
    if a < b:
        return ggT_mxy(b, a)

    m = [a, b]
    x = [1, 0]
    y = [0, 1]
    while m[-1] != 0:
        q = math.floor(m[-2]/m[-1])
        m.append((-q)*m[-1]+m[-2])
        x.append(x[-2]-(q*x[-1]))
        y.append(x[-2]-(q*y[-1]))
        if len(m) > 32:
            m = m[-5:]
            x = x[-5:]
            y = y[-5:]
    return m[-2], x[-2], y[-2]


def ggT(a: int, b: int) -> int:
    return ggT_mxy(a, b)[0]


def solve_dio(a: int, b: int, c: int) -> Tuple[int, int]:
    #TODO fix this
    m, x, y = ggT_mxy(a, b)
    q = c//(a*x+b*y)
    return q*x, q*y


def kgV(a: int, b: int) -> int:
    return (a*b)//ggT(a, b)


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

    print("\nTEST solve_dio:")
    for i in range(5):
        a = random.randint(100, 10**3)
        b = random.randint(100, 10**3)
        c = random.randint(100, 10**3)
        while c < a or c < b:
            c = random.randint(10000, 10**6)
        x, y = solve_dio(a, b, c)
        print(a*x + b*y == c)

    print("\nTEST kgV:")
    def brut_kgV(a: int, b: int) -> int:
        if a > b:
            return brut_kgV(b, a)
        for i in range(a, (a*b)+1):
            if i%a == 0 and i%b == 0:
                return i
    for i in range(5):
        a = random.randint(100, 10**3)
        b = random.randint(100, 10**3)
        print(kgV(a, b) == brut_kgV(a, b))
