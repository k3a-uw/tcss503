import numpy as np


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_dp(n):
    if n < 2:
        return n
    solution = [0] * (n+1)
    solution[0] = 0
    solution[1] = 1
    for i in range(2,n+1):
        solution[i] = solution[i-1] + solution[i-2]

    return solution[-1]

def job_selection_w_recover(calendar):
    size = len(calendar)
    j = [0] * size
    s = [False] * size
    j[0] = calendar[0]
    s[0] = True
    j[1] = max(calendar[0], calendar[1])
    s[1] = calendar[1] > calendar[0]

    for i in range(2, size):
        with_last = j[i-2] + calendar[i]
        with_out_last = j[i-1]
        j[i] = max(with_last, with_out_last)
        s[i] = with_last > with_out_last

    days_worked = job_selection_recover(s)
    return days_worked, j[-1]

def job_selection_recover(job_solution):
    a = []
    i = len(job_solution) - 1

    while i >= 0:
        if job_solution[i]:
            a.append(i)
            i -= 2
        else:
            i -= 1
    return a

def job_selection_no_recover(calendar):
    size = len(calendar)
    j = [0] * size
    days_worked = [None] * size  # CAN ALSO MAINTAIN THE DAYS WORKED TO NOT REQUIRE THE RECOVERY (LIKE CHANGE MAKING)
    j[0] = calendar[0]
    days_worked[0] = [0]
    j[1] = max(calendar[0], calendar[1])
    days_worked[1] = [1 if calendar[1] > calendar[0] else 0]

    for i in range(2, size):
        with_last = j[i-2] + calendar[i]
        with_out_last = j[i-1]
        j[i] = max(with_last, with_out_last)
        if with_last > with_out_last:
            days_worked[i] = days_worked[i-2].copy()
            days_worked[i].append(i)
        else:
            days_worked[i] = days_worked[i-1].copy()

    return days_worked[-1], j[-1]

def knapsack(weights, values, capacity):
    solution = np.zeros((len(weights), capacity+1))
    # INITIALIZE THE FIRST ITEM
    for j in range(capacity+1):
        solution[0, j] = values[0] if j >= weights[0] else 0

    for i in range(1, len(weights)):
        for j in range(capacity+1):
            if j - weights[i] >= 0:  # IF THIS ITEM CAN FIT
                with_item = solution[i-1, j-weights[i]] + values[i]
            else:
                with_item = -1

            without_item = solution[i-1,j]
            solution[i, j] = max(without_item, with_item)

    return solution

def knapsack_recovery(solution, weights, values):
    rows, cols = solution.shape

    curr_row = rows - 1
    curr_col = cols - 1

    result = []

    curr_val = solution[curr_row, curr_col]

    while curr_val > 0:
        if curr_row == 0:
            result.append(curr_row)
            break
        elif curr_val != solution[curr_row - 1, curr_col]:
            result.append(curr_row)
            curr_val = curr_val - values[curr_row]
            curr_col = curr_col - weights[curr_row]
            curr_row -= 1
        else:
            curr_row -= 1

    return result




if __name__ == "__main__":
    # FIB DEMO:
    # for i in range(10):
    #     print(fib(i))
    # for i in range(50):
    #     print(fib_dp(i))

# JOB SELECTION DEMO
#     p = [15, 46, 43, 51, 92, 72, 61, 41, 39, 40, 82, 79, 42, 51]
#     days_worked, dollars = job_selection_no_recover(p)
#
#     print(f"By Working days: {days_worked} you can earn {dollars}")

    #
    w = [10,4,2,6,7,4,1,3]
    v = [1,1,5,6,7,2,4,1]
    c = 13
    solution = knapsack(w,v,c)
    print(solution)
    kp_solution = knapsack_recovery(solution, w, v)
    print(kp_solution)

    w = [5,4,1]
    v = [150, 100, 10]
    c = 10
    solution = knapsack(w,v,c)

    print(solution)
    kp_solution = knapsack_recovery(solution, w, v)

    t = 0
    for val in kp_solution:
        t += v[val]

    print(f"Total Value: {t}  but solution says: {solution[-1,-1]}")
    print(kp_solution)