import numpy as np

def recursive_matrix_mult(A, B):
    """
    Recursively multiplies sub matrices of A and B
    :param a: The first Matrix A implemented as a np.array
    :param b: The second Matrix B implemented as a np.array
    :return: The product of a and b
    """
    a = np.array(A)
    b = np.array(B)
    if len(a) == 1:
        return a*b

    n = a.shape[0] // 2
    a0 = a[:n, :n]  # UPPER LEFT
    a1 = a[:n, n:]  # UPPER RIGHT
    a2 = a[n:, :n]  # LOWER LEFT
    a3 = a[n:, n:]  # LOWER RIGHT

    b0 = b[:n, :n]  # UPPER LEFT
    b1 = b[:n, n:]  # UPPER RIGHT
    b2 = b[n:, :n]  # LOWER LEFT
    b3 = b[n:, n:]  # LOWER RIGHT

    c0 = recursive_matrix_mult(a0, b0) + recursive_matrix_mult(a1, b2)
    c1 = recursive_matrix_mult(a0, b1) + recursive_matrix_mult(a1, b3)
    c2 = recursive_matrix_mult(a2, b0) + recursive_matrix_mult(a3, b2)
    c3 = recursive_matrix_mult(a2, b1) + recursive_matrix_mult(a3, b3)

    top = np.hstack((c0, c1))
    bottom = np.hstack((c2, c3))

    return np.vstack((top, bottom))

def basic_smoke_test():
    smoke1 = [[1, 2], [3, 4]]
    smoke2 = [[5, 6], [7, 8]]
    result = strassens(smoke1, smoke2)
    expected = np.array([[19, 22], [43, 50]])
    assert(np.array_equal(result, expected))
    print("First test passed")

    smoke3 = [[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10], [10, 11, 12, 13]]
    result = recursive_matrix_mult(smoke3, smoke3)
    expected = np.array([[70, 80, 90, 100], [136, 158, 180, 202], [202, 236, 270, 304], [268, 314, 360, 406]])
    assert(np.array_equal(result, expected))
    print("Second test passed")

## THE STUDENT SHOULD IMPLEMENT STRASSENS MATRIX MULTIPLICATION ALGORITHM
def strassens(A, B):
    """
    Uses Strassen’s method for matrix multiplication to return the product of the two
    provided Matrices A and B.
    :param A: the first matrix to multiply. Implemented as a np.array
    :param B: The second matrix to multiply. Implemented as a np.array
    :return: The product of A and B
    """
    pass



if __name__ == "__main__":
    # NOTE THIS IS JUST A BASIC SMOKE TEST.  TO RUN THE FULL TEST SUITE THAT WILL BE USED FOR GRADING USE THE INCLUDED
    # StrassensTester.py.  RUN StrassensTester.py WITH THE PROPER IMPORT STATEMENT IN LINE 2 TO SEE THE RESULTS.
    basic_smoke_test()