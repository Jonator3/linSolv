from typing import List


def multiply(vals: List[float]) -> float:
    if len(vals) == 1:
        return vals[0]
    else:
        return vals[0] * multiply(vals[1:])


def gauss_stair(mat: List[List[float]]) -> List[List[float]]:
    mat = [line.copy() for line in mat]
    n = len(mat)
    
    # TODO make stair form
        
    return mat


def gauss_normal(mat: List[List[float]]) -> List[List[float]]:
    mat = [line.copy() for line in mat]
    n = len(mat)
    
    # TODO normalize
    
    return mat
    

def lin_solve(mat: List[List[float]]) -> List[List[float]] | None:
    mat = gauss_stair(mat)
    mat = gauss_normal(mat)

    # TODO check for resolvability

    n = len(mat)
    mat = [line[n:] for line in mat]
    
    return mat


def det(mat: List[List[float]]) -> float:
    mat = [line.copy() for line in mat]
    n = len(mat)
    for i in range(n):
        if len(mat[i]) != n:
            raise ValueError("Matix is not a square matrix")
    
    mat = gauss_stair(mat)
    return multiply([mat[i][i] for i in range(n)])