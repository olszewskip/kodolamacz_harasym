from math import sqrt

def euclidean_distance(A, B):
    """
    >>> euclidean_distance((0,0), (1,0))
    1.0

    >>> euclidean_distance((0,0), (1,1))
    1.4142135623730951

    >>> euclidean_distance((0,1), (1,1))
    1.0

    >>> euclidean_distance((0,10), (1,1))
    9.055385138137417
    """
    squares = [(A[i] - B[i])**2 for i in range(len(A))]
    return sqrt(sum(squares))


