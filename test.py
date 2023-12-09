import random

import linSolv


def str_stuff(s, l=6, c=" "):
    while len(s) < l:
        s = c + s
    return s


def mat_print(mat):
    for row in mat:
        for elem in row:
            print("|"+str_stuff(str(round(elem, 2))), end='')
        print("|")
    print("")


def rsvw(w, solv_mat):
    solv_mat = linSolv.back_substitution(solv_mat)

    r = solv_mat[0][0]*w + solv_mat[0][1]
    s = solv_mat[1][0]*w + solv_mat[1][1]
    v = solv_mat[2][0]*w + solv_mat[2][1]

    return r, s, v, w


def rs_dot(r, s):
    return round(1 + 4*r + 7*s, 3), round(2 + 5*r + 8*s, 3), round(3 + 6*r + 9*s, 3)


def vw_dot(v, w):
    return round(3 + 12*v + 8*w, 3), round(2 + 9*v + w, 3), round(1 + 24*v + 9*w, 3)


mat = [
    [4, 7, -12, -8,  2],
    [5, 8, -9,  -1,  0],
    [6, 9, -24, -9, -2],
]

solv = linSolv.lin_solve(mat)

mat_print(solv)

print("Test 1")
for i in range(5):
    r, s, v, w = rsvw(random.randint(-100, 100), solv)
    print(rs_dot(r, s) == vw_dot(v, w))
print("")


print("Test 2")
mat = [
    [1, 0, 0, 3, 14],
    [0, 1, 0, 2, 23],
    [0, 0, 1, 1, -5],
    [3, 2, 1, 0, 0]
]

solv = linSolv.lin_solve(mat)
x, y, z, r = [round(line[0], 2) for line in solv]

print(3*r+x == 14)
print(2*r+y == 23)
print(r+z == -5)
print("")

print("Test 3")
for i in range(5):
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    z = random.randint(-100, 100)
    mat = [
        [x, y, z],
        [x, y, z-1]
    ]
    solv = linSolv.lin_solve(mat)
    print(solv is None)
print("")

print("Test 4")
for i in range(5):
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    v = random.randint(-100, 100)
    w = random.randint(-100, 100)
    mat = [
        [x, 0, v],
        [0, y, w],
        [0, 0, 0]
    ]
    solv = linSolv.lin_solve(mat)
    print(len(solv) == 2, round(solv[0][0]*x, 3) == v and round(solv[1][0]*y, 3) == w)
