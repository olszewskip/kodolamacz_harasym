def matrix_multiplication(A, B):
    """
    >>> A = [[1, 0], [0, 1]]
    >>> B = [[4, 1], [2, 2]]
    >>> matrix_multiplication(A, B)
    [[4, 1], [2, 2]]
    """
    assert(len(A[0]) == len(B))
    n = len(B)

    result_rows = []

    for Arow in A:
        result_row = []

        for Bcol_idx in range(n):
            products = [Arow[i] * B[i][Bcol_idx] for i in range(n)]
            result_row.append(sum(products))

        result_rows.append(result_row)

    return result_rows



import numpy as np

def matrix_multiplication(A, B):
    """
    >>> A = [[1, 0], [0, 1]]
    >>> B = [[4, 1], [2, 2]]
    >>> matrix_multiplication(A, B)
    [[4, 1], [2, 2]]
    """

    A_arr = np.array(A)
    B_arr = np.array(B)
    #C_arr = np.matmul(A_arr, B_arr)
    C_arr = A_arr @ B_arr
    C = [list(C_arr_row) for C_arr_row in C_arr]

    return C
