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
    return 1 + 4*r + 7*s, 2 + 5*r + 8*s, 3 + 6*r + 9*s


def vw_dot(v, w):
    return 3 + 12*v + 8*w, 2 + 9*v + w, 1 + 24*v + 9*w



mat = [
    [4, 7, -12, -8,  2],
    [5, 8, -9,  -1,  0],
    [6, 9, -24, -9, -2],
]

solv = linSolv.lin_solve(mat)

mat_print(solv)

r, s, v, w = rsvw(5, solv)

print(rs_dot(r, s))
print(vw_dot(v, w))
