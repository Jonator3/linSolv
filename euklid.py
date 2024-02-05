import math
import random


def ggt(a, b):
    if a < b:
        return ggt(b, a)

    q = math.floor(a / b)

    x = a - q * b

    if x == 0:
        return b

    return ggt(b, x)


def euklid(a, b, x_prev=None, y_prev=None, x_cur=1, y_cur=0, q_prev=None):
    if a < b:
        return euklid(b, a, x_prev=x_prev, y_prev=y_prev, x_cur=x_cur, y_cur=y_cur)

    q = math.floor(a / b)

    x = a - q * b

    if q_prev is None:
        return euklid(b, x,
                      x_prev=x_cur,
                      y_prev=y_cur,
                      q_prev=q,
                      x_cur=0,
                      y_cur=1)

    x_next = x_prev - q_prev * x_cur
    y_next = y_prev - q_prev * y_cur

    if x == 0:
        return b, x_next, y_next

    return euklid(
        b, x,
        x_prev=x_cur,
        y_prev=y_cur,
        q_prev=q,
        x_cur=x_next,
        y_cur=y_next,
    )


print(f"{euklid(420, 255) = }")


def solve_dio(c, a, b):
    ggt_, xk, yk = euklid(a, b)

    q = c / ggt_

    return q * xk, q * yk


print(f"{solve_dio(1320, 420, 255) = }")


def solve_dio_check(c, a, b):
    x, y = solve_dio(c, a, b)
    return x, y, f"{a*x + b*y = }"


print(f"{solve_dio_check(414, 257, 109) = }")

print("\nTEST ggT:")


def brut_ggt(a: int, b: int) -> int:
    if a < b:
        return brut_ggt(b, a)
    for i in range(b):
        c = b - i
        if a % c == 0 and b % c == 0:
            return c


for i in range(5):
    a = random.randint(100, 10 ** 5)
    b = random.randint(100, 10 ** 5)

    print(ggt(a, b) == brut_ggt(a, b))
