import math
import random


def ggt(a, b):

    if a < b:
        return ggt(b, a)

    q = math.floor(a/b)

    x = a - q * b

    if x == 0:
        return q

    return ggt(b, x)



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

    print(ggt(a, b) == brut_ggt(a, b))