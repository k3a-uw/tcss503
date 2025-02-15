import numpy as np


class NQueens:
    """
    Create a Board of N x N squared and solve.
    """

    def __init__(self, size):
        self.size = size
        self.solution_stack = []
        self.solutions = 0

    def find_solution(self, find_all=True):
        self.solutions = 0
        for col in range(self.size):
            solution = [-1 for _ in range(self.size)]
            solution[0] = col  # SEED THE INITIAL SOLUTION
            self.solution_stack.append(solution)

        while self.solution_stack:
            curr_solution = self.solution_stack.pop()
            curr_row = sum(x != -1 for x in curr_solution)
            for col in range(self.size):
                if self.can_place(curr_solution, col):
                    new_solution = curr_solution.copy()
                    new_solution[curr_row] = col
                    if curr_row + 1 == self.size:
                        print("Found Solution!")
                        print(self.draw_board(new_solution))
                        if find_all:
                            self.solutions += 1
                            break
                        else:
                            return

                    self.solution_stack.append(new_solution)

        print(f"{self.solutions} Solutions Found")
        return

    def solve_recursive(self):
        # SETUP THE INITIAL EMPTY SOLUTION
        solution = [-1 for _ in range(self.size)]

        # START TO SOLVE THE EMPTY SOLUTION BY PLACING A QUEEN IN ROW 0
        return self._solve(solution, 0)

    def _solve(self, solution, row):
        # TRY TO PLACE A QUEEN IN EACH COLUMN
        for col in range(self.size):
            if self.can_place(solution, col): # IF I CAN, ADD IT TO SOLUTION AND THEN CALL ON NEXT ROW.
                solution[row] = col
                if row + 1 == self.size:    # WE HIT OUR GOAL AND PLACED THE LAST ONE.
                    return solution
                result = self._solve(solution.copy(), row + 1) # TRY TO SOLVE THE NEXT ROW WITH THIS NEW SOLUTION.
                if result:
                    return result
            # IF YOU CANNOT PLACE, JUST GO TO THE NEXT COLUMN.
        # IF YOU ARE HERE, YOU HAVE TRIED TO PLACE ALL QUEENS IN THAT ROW UNSUCCESSFULLY SO JUST RETURN NONE

    def can_place(self, solution, col):
        num_rows = sum(x != -1 for x in solution)
        for row in range(num_rows):
            if solution[row] == col:  # IF ANOTHER QUEEN IS IN SAME COLUMN
                return False
            if solution[row] - (num_rows - row) == col:
                return False
            if solution[row] + (num_rows - row) == col:
                return False
        return True

    def draw_board(self, solution):
        if not solution:
            return "[No Solution Provided]"

        board = ""
        for r in range(self.size):
            board += f"{r}: "
            for c in range(self.size):
                if solution[r] == c:
                    board += "|X"
                else:
                    board += "| "
            board += "|\n"
        return board


class MatrixGraph:
    """ A Python Implementation of a Basic Directed Graph.
    """
    def __init__(self, v_count):
        self.V = v_count
        self.adj_matrix = np.zeros((self.V, self.V))

    def _can_color(self, color, solution, vertex):
        for col in range(self.V):   # LOOP THROUGH A ROW OF THE ADJACENCY MATRIX
            if self.adj_matrix[vertex, col] == 1 and solution[col] == color:
                return False

        return True

    def _color(self, colors, solution, vertex):

        for color in colors:
            if self._can_color(color, solution, vertex):  # CHECK SOLUTION TO SEE IF COLOR IS ALLOWED
                solution[vertex] = color
                if vertex == self.V - 1: # WE HAVE COLORED OUR LAST NODE
                    return solution

                if self._color(colors, solution, vertex+1):
                    return solution

    def m_color(self, colors):
        solution = [None] * self.V

        result = self._color(colors, solution, 0)
        if result:
            print(f"Solution Found!: {result}")
        else:
            print("No Solutions")


if __name__ == "__main__":
    g = MatrixGraph(4)
    colors = ['red', 'green', 'blue']
    g.adj_matrix = np.array([
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ])
    g.m_color(colors)

    big_g = MatrixGraph(10)
    # BELOW IS A LINK TO THE VIZ REPRESENTATION OF THE BELOW GRAPH
    # https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Petersen_graph_3-coloring.svg/220px-Petersen_graph_3-coloring.svg.png
    big_g.adj_matrix = np.array([
        [0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 1, 0, 0]
    ])

    big_colors = ['green', 'red', 'white']
    big_g.m_color(big_colors)



    print("\n\n")
    # USE THE RECURSIVE VERSION TO GET JUST ONE OF THE ANSWERS.
    print("Recursive Call to get one solution quickly.:")
    x = NQueens(size=10)
    results = x.solve_recursive()
    print(x.draw_board(results))


    print("\n\n Iterative Call to get all solution.")
    # SOLVE THE N QUEENS PROBLEM USE ITERATIVE APPROACH TO GET ALL SOLUTIONS.
    b = NQueens(size=5)
    b.find_solution(find_all=True)

