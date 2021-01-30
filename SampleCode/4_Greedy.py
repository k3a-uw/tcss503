def change_making_greedy(target, denoms):
    r = []
    for denom in sorted(denoms, reverse=True):
        while sum(r) + denom <= target:
            r.append(denom)
    return r if sum(r) == target else None

def change_making_dynamic(target, denoms):
    """
    Uses Dynamic Programming to determine the minimum coins required from the provided denominations to generate the
    targeted amount.
    :param target: An integer target amount of change to create.
    :param denoms: A list of integers representing the denominations of change accessible to the algorithm.
    :return: A minimal list of coins needed to reach the target total.  If exact change cannot be made, then `None`
    is returned.
    """
    data = [None] * (target+1)
    data[0] = []
    for i in range(1, target+1):
        # LOOP THROUGH EACH VALUE UP TO THE TARGET
        curr_min = None
        for denom in denoms:
            back_val = i - denom
            if back_val >= 0:  # IF YOU ARE ABLE TO SUBTRACT THE CURRENT DENOM FROM THE VALUE.
                if data[back_val] is None:
                    continue # PREVIOUS CALCULATION IS INVALID AND CANNOT BE USED.
                curr = data[back_val].copy()
                curr.append(denom)
                if curr_min is None or len(curr) < len(curr_min):
                    curr_min = curr
        data[i] = curr_min

    return(data[target])


change_making_greedy(30, [1, 15, 25])
x = change_making_dynamic(30, [1, 15, 25])
print(f"Basic, 15, 15 {x}")

y = change_making_dynamic(14, [7, 13, 25])
print(f"Partial Gaps, 7,7: {y}")

z = change_making_dynamic(15, [7, 13, 25])
print(f"Should Be None: {z}")

