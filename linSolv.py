from typing import List


def multiply(vals: List[float]) -> float:
    if len(vals) == 1:
        return vals[0]
    else:
        return vals[0] * multiply(vals[1:])


def back_substitution(mat: List[List[float]]) -> List[List[float]]:
    mat = [line.copy() for line in mat]
    for i in range(len(mat)):
        mat[i] = [-val for val in mat[i][:-1]] + [mat[i][-1]]
    return mat


def gauss_stair(mat: List[List[float]]) -> List[List[float]]:
    mat = [line.copy() for line in mat]
    n = len(mat)

    for i in range(1, n):
        val_i = mat[i-1][i-1]
        # TODO what if val_i == 0 ?
        for j in range(i, n):
            faktor = mat[j][i-1] / val_i
            for k in range(len(mat[j])):
                mat[j][k] = mat[j][k]-(faktor * mat[i-1][k])

    return mat


def gauss_normal(mat: List[List[float]]) -> List[List[float]]:
    mat = [line.copy() for line in mat]
    n = len(mat)

    # make diagonal 1s
    for i in range(n):
        faktor = 1 / mat[i][i]
        for k in range(len(mat[i])):
            mat[i][k] = faktor * mat[i][k]
            if abs(mat[i][k]) == 0:
                mat[i][k] = 0.0

    # remove upper-right values
    for i in range(n):
        line = n-(i+1)
        for j in range(line):
            faktor = mat[j][line]
            for k in range(len(mat[j])):
                mat[j][k] = mat[j][k]-(faktor * mat[line][k])
                if abs(mat[j][k]) == 0:
                    mat[j][k] = 0.0

    return mat
    

def lin_solve(mat: List[List[float]]) -> List[List[float]] | None:
    mat = gauss_stair(mat)

    del_list = []  # list off all 0 rows, ready to be removed
    for i in range(len(mat)):
        if len([val for val in mat[i][:-1] if val != 0]) == 0:
            if mat[i][-1] != 0:
                return None
            else:
                del_list.append(i)

    # remove rows with all 0:
    del_list.sort(reverse=True)
    for i in del_list:
        del mat[i]
    del del_list

    mat = gauss_normal(mat)

    n = len(mat)
    mat = [line[n:] for line in mat]
    
    return mat


def det(mat: List[List[float]]) -> float:
    mat = [line.copy() for line in mat]
    n = len(mat)
    for i in range(n):
        if len(mat[i]) != n:
            raise ValueError("Matrix is not a square matrix")
    
    mat = gauss_stair(mat)
    return multiply([mat[i][i] for i in range(n)])
