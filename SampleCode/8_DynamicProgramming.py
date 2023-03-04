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

    return A

def subset_recover(solution, values):
    rows, cols = solution.shape
    curr_row = rows - 1
    curr_col = target = cols - 1
    curr_tot = 0
    results = []

    # TRIVIAL CASE IF LOWER RIGHT IS NOT TRUE
    # RETURN EMPTY AS NO SUBSET EXISTS
    if not solution[curr_row, curr_col]:
        return []

    while curr_tot < target:
        # IF AT THE FIRST ROW, TAKE THE VALUE AUTOMATICALLY
        if curr_row == 0:
            results.append(values[curr_row])
            curr_tot += values[curr_row]
        # IF THE VALUE OF THE PREVIOUS ROW IS FALSE
        # INCLUDE THE VALUE OF THE ROW AND MOVE OVER
        if not solution[curr_row - 1, curr_col]:
            results.append(values[curr_row])
            curr_tot += values[curr_row]
            curr_col -= values[curr_row]

        curr_row -= 1

    return results


def subset_sum_w_solution(s, t):
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

    curr_row = n - 1
    curr_col = t
    curr_tot = 0
    results = []

    # TRIVIAL CASE IF LOWER RIGHT IS NOT TRUE
    # RETURN EMPTY AS NO SUBSET EXISTS
    if not A[curr_row, curr_col]:
        return []

    while curr_tot < t:
        # IF THE VALUE OF THE PREVIOUS ROW IS FALSE
        # INCLUDE THE VALUE OF THE ROW AND MOVE OVER
        if curr_row == 0:
            results.append(s[curr_row])
            curr_tot += s[curr_row]
        if not A[curr_row - 1, curr_col]:
            results.append(s[curr_row])
            curr_tot += s[curr_row]
            curr_col -= s[curr_row]

        curr_row -= 1

    return results

v = [2,3,5,7,9]
x = subset_sum(v, 12)

for test in range(28):
    x = subset_sum_w_solution(v,test)
    # y = subset_recover(x, v)
    print(f"Target: {test}, Solution: {x}")



