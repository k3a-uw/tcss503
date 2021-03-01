import numpy as np
def subset_sum(s, t):
    n = len(s)
    A = np.empty((n, t+1))

    # POPULATE FIRST COLUMN WITH TRUE
    A[:, 0] = True

    for j in range(1, t+1):
        A[0, j] = s[0] == j

    for i in range(1, n):
        for j in range(1, t+1):
            if j >= s[i]:
                A[i, j] = A[i - 1, j] or A[i - 1, j - s[i]]
            else:
                A[i, j] = A[i - 1, j]

    return A[-1, -1]


x = subset_sum([2,3,5,7,9], 12)
print(x)