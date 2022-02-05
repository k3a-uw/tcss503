import numpy as np
import time
import pandas as pd
import matplotlib.pyplot as plt
import random


def karatsuba(x, y):
    """ Recursive implementation of Karatsuba's Fast Mulciplication Algoritihm

    :param x: The first integer
    :param y: The second integer
    :return: The product of x * y
    """
    if x < 10 or y < 10:
        return x*y

    m = max(len(str(x)), len(str(y))) // 2

    x_high = x // 10**m
    x_low = x % 10**m
    y_high = y // 10**m
    y_low = y % 10**m

    z0 = karatsuba(x_low, y_low)
    z1 = karatsuba(x_low + x_high, y_low + y_high)
    z2 = karatsuba(x_high, y_high)

    return z2 * 10 ** (2 * m) + (z1 - z2 - z0) * 10 ** m + z0


def karat_compare(max_size, tests):
    samples = []
    test_sizes = np.linspace(1,max_size, tests).astype(int)
    standard_results = []
    karatsuba_results = []
    for test_size in test_sizes:
        x_str = ''
        y_str = ''
        for x in range(test_size):
            x_str += str(random.randint(0,9))
            y_str += str(random.randint(0,9))
        samples.append((int(x_str), int(y_str)))
    print(f"Samples Generated: {len(samples)}, with max size: {max_size}")

    for sample, test_size in zip(samples, test_sizes):
        print(f"Attempting numbers of 10^{test_size}")
        x = sample[0]
        y = sample[1]

        t_start = time.perf_counter()
        r = x * y
        standard_results.append(time.perf_counter() - t_start)

        t_start = time.perf_counter()
        r = karatsuba(x, y)
        karatsuba_results.append(time.perf_counter() - t_start)

    plt.plot(test_size, standard_results, label="python native")
    plt.plot(test_size, karatsuba_results, label="karatsuba")
    plt.xlabel("10^x")
    plt.ylabel("Seconds")
    plt.legend()
    plt.show()


def naive_matrix_multiplication_lists(a, b):
    """
    Uses nested loops to calculate AB
    :param a: An MxN matrix of numbers.
    :param b: An NxP matrix of numbers.
    :return: An MxP matrix of numbers which is the product: AB.
    """
    M = len(a)
    N = len(a[0])
    if len(b) != N:
        raise ValueError("The Matrices Provide are not the proper shape.")
    P = len(b[0])

    c = [[0 for i in range(P)] for j in range(M)]

    for i in range(0,M):
        for j in range(0,P):
            for k in range(0,N):
                c[i][j] += a[i][k] * b[k][j]
    return c


def naive_matrix_multiplication_np(a,b):
    M, N = a.shape
    n, P = b.shape

    if N != n:
        raise ValueError("The Matrices Provide are not the proper shape.")

    c = np.zeros((M,P))

    for i in range(0,M):
        for j in range(0,P):
            for k in range(0,N):
                c[i][j] += a[i][k] * b[k][j]
    return c




if __name__ == "__main__":
    a = [[1, 2, 5],
         [3, 4, 6]]

    b = [[5, 6],
         [7, 8],
         [1, 1]]

    c = naive_matrix_multiplication_lists(a, b)
    print("List Results:\n", c)

    A = np.array(a)
    B = np.array(b)
    C = naive_matrix_multiplication_np(A, B)
    print("NP Array Results:\n", C)

    expected_results = np.array([[24, 27], [49, 56]])
    print("Expected Results:\n", expected_results)

