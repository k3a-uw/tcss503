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


def local_hill_climbing(the_function, start, alpha=0.5, maximize=True, max_iterations=1000):
    """
    A function to iterate over units of alpha to return the value that maximizes the value of the provided function using
    local hill climbing.
    :param the_function: A function containing a single input.
    :param start: The initial value to use to see the hill climb
    :param alpha: (Optional) Provides the magnitude of change per iteration.
    :param maximize: (Optional) When True the algorithm will seek a maximum value of the function, minimum value otherwise.
    :param max_iterations: (Optional) The maximum iterations before halting.
    """

    # INITIALIZE VARIABLES FOR PREPARING TO LOOP
    iterations = 0
    curr_value = start

    if max_iterations <= 0:
        raise ValueError("Max Iterations must be a positive number.")

    while iterations < max_iterations:

        curr_result = the_function(curr_value)
        left_result = the_function(curr_value - alpha)
        right_result = the_function(curr_value + alpha)

        if not maximize:
            curr_result = curr_result * -1
            left_result = left_result * -1
            right_result = right_result * -1

        if right_result >= left_result:
            if right_result <= curr_result:  # LOCAL MAXIMA/MINIMA
                break
            else:  # KEEP MOVING RIGHT
                curr_value += alpha
                iterations += 1
        else:  # LEFT IS BIGGER THAN RIGHT
            if left_result <= curr_result:  # LOCAL MAXIMA/MINIMA
                break
            else:
                curr_value -= alpha
                iterations += 1

    if not maximize:  # RESET CURRENT RESULT TO * -1
        curr_result = curr_result * -1

    return curr_value, curr_result


def parabola(x):
    return -(x-5)**2 + 3


def step_function(x):
    """
    This function makes a plateau that we can test edge cases.  From -inf to 1, it returns x=y,  Then flattens from
    1 to 5 and then decreases from 5 on.
    """
    if x < 1:
        return x
    elif x < 5:
        return 1
    elif x >= 5:
        return -x+6


if __name__ == '__main__':
    print("===TESTING PARABOLA ====")

    # START WITH THE PARABOLA JUST TO SEE IF WE GET THE LOCAL MAXIMA WITH DIFFERENT STARTS
    tests = [(0, "LEFT OF MAX POINT"),
             (10, "RIGHT OF MAX POINT"),
             (5, "EXACTLY ON MAX POINT"),
             (4.7, "LESS THAN AN ALPHA AWAY")]

    x = 0
    for test in tests:
        start = test[0]
        x += 1
        results = local_hill_climbing(parabola, start)
        print(f"TEST{x}: {test[1]}")
        print(f"Starting at {start}, the max result is {results[1]} given an input value of {results[0]}\n")


    # ADDITIONAL EXPERIMENTS
    start = 4.7
    results = local_hill_climbing(parabola, start, alpha=0.001, max_iterations=10000)
    print("Final Test: START LESS THAN AN ALPHA AWAY WITH LOWER ALPHA AND HIGHER ITERATIONS")
    print(f"Starting at {start}, the max result is {results[1]} given an input value of {results[0]}\n\n")



    print("===TESTING STEP FUNCTIONS ====")

    # STEP FUNCTION TESTING
    tests = [(-1, "LEFT OF LEFT SHOULDER, Max:True", True),
             (-1, "LEFT OF LEFT SHOULDER, Max:False", False),
             (1, "EXACTLY ON LEFT SHOULDER, Max:True", True),
             (1, "EXACTLY ON LEFT SHOULDER, Max:False", False),
             (3, "MID-PLATEAU Max=True", True),
             (3, "MID-PLATEAU Max=True", False),
             (5, "EXACTLY ON RIGHT SHOULDER, Max:True", True),
             (5, "EXACTLY ON RIGHT SHOULDER, Max:False", False),
             (10, "RIGHT OF RIGHT SHOULDER, Max:True", True),
             (10, "RIGHT OF RIGHT SHOULDER, Max:False", False)
             ]

    x = 0
    for test in tests:
        start = test[0]
        x += 1
        max = test[2]
        results = local_hill_climbing(step_function, start, maximize=max)
        print(f"TEST{x}: {test[1]}")
        print(f"Starting at {start}, the result is {results[1]} given an input value of {results[0]}\n")





    change_making_greedy(30, [1, 15, 25])
    x = change_making_dynamic(30, [1, 15, 25])
    print(f"Basic, 15, 15 {x}")

    y = change_making_dynamic(14, [7, 13, 25])
    print(f"Partial Gaps, 7,7: {y}")

    z = change_making_dynamic(15, [7, 13, 25])
    print(f"Should Be None: {z}")

