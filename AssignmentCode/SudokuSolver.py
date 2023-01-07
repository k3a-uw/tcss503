import numpy as np
import random     # USED FOR THE BOARD GENERATOR


class SudokuSolver:
    """ A Python implementation of a SudokoSolver, uses a backtracking method to solve a Sudoku Puzzle
    with bruteforce.  For each empty cell, the algorithm will attempt to place a digit and them move to
    the next cell.  If a dead cell is found (no digits can be placed). The previously placed digit will
    be changed."""

    def __init__(self, section_size=3):
        """
        Creates a new "empty" Sudoku Board (an empty cell is represented with -1)
        :param section_size: The size of the inner section of a Sudoku Board.  For example, a standard board contains
        9 squares of 3x3 each.  Therefor the "section_size" is 3.  A section_size of 4 would be a 4x4 board.
        """

        if section_size < 2:
            raise ValueError("section_size must be at least 2.")

        self.section_size = section_size
        self.board_size = section_size ** 2
        self.board = np.empty((self.board_size, self.board_size))
        self.board.fill(-1)
        self.digits = range(1, self.board_size + 1)
        self.board_solved = None

    def __str__(self):
        """
        Magic function to draw the board that is represented by the class.
        :return: A string representation of the board that is represented by the class.
        """

        return self.draw_puzzle(board=self.board)

    def draw_puzzle(self, board, padding=1, empty_char=" "):
        """
        Function that will return a string representation of a provided board.
        :param board: The board to be drawn
        :param padding: The amount of spaces to place before and after each number.  Defaults to 1
        :param empty_char: The character to use in an empty space.  Defaults to " "
        :return: A string representation of the board
        """

        num_width = len(str(self.board_size))
        cell_width = num_width + (padding * 2)
        empty_char = empty_char * num_width
        h_padding = " " * padding

        v_line_char = "|"
        h_line_char = "-"
        x_line_char_major = "X"
        x_line_char_minor = "+"
        h_cell_line = h_line_char * cell_width

        board_str = ""
        for row in range(self.board_size):
            if row % self.section_size == 0:
                # EVERY SECTION DRAW A BORDER
                boarder_line = ""
                for i in range(self.section_size):
                    boarder_line += x_line_char_major + x_line_char_minor.join([h_cell_line] * self.section_size)
                boarder_line += x_line_char_major + "\n"
                board_str += boarder_line

            # NUMBER LINE
            number_line = ""
            for i in range(self.board_size):
                curr_val = int(board[row, i])
                if curr_val == -1:
                    curr_num_str = f"{h_padding}{empty_char}{h_padding}"
                else:
                    curr_num_str = f"{h_padding}{curr_val:{num_width}d}{h_padding}"
                number_line += f"{v_line_char}{curr_num_str}"

            number_line += f"{v_line_char}\n"
            board_str += number_line

        # ONCE ALL DONE, DRAW ONE FINAL BOARDER LINE
        boarder_line = ""
        for i in range(self.section_size):
            boarder_line += x_line_char_major + x_line_char_minor.join([h_cell_line] * self.section_size)

        boarder_line += x_line_char_major + "\n"
        board_str += boarder_line

        return board_str

    def draw_solution(self):
        """
        Draws the puzzle identified as the current solution to the puzzle.
        :return: A string representation of the puzzle.
        """

        return self.draw_puzzle(self.board_solved)

    def generator(self, num_to_place=None, seed=None):
        """
        Resets the SudokuPuzzle with a new randomly generated puzzle.  Note, this is entirely random and _may_ generate
        unsolvable puzzles.  It is also possible to infinitely loop
        :param num_to_place: The number of cells to populate initially.  If omitted the approximately one third of the
        cells will be populated.
        :param seed: Used to set the random seed to allow for repeatable generation of boards.  For example, seed=2000
        will always return the same board.
        :return: None
        """

        ERROR_RELEASE_VALVE = 20
        random.seed(seed)
        if num_to_place is None:
            num_to_place = (self.board_size ** 2) // 3

        self.board = np.empty((self.board_size, self.board_size))
        self.board.fill(-1)
        placed = 0
        while placed < num_to_place:
            row = random.randrange(0, self.board_size)
            col = random.randrange(0, self.board_size)
            val = random.randrange(0, self.board_size) + 1
            if self.can_place(self.board, row, col, val):
                missed = 0
                self.board[row, col] = val
                placed += 1
            else:
                missed += 1
                if missed > ERROR_RELEASE_VALVE:
                    self.reset()
                    placed = 0

    def loader(self, board):
        """
        Resets the SudokoBoard with the provided board.
        :param board: A 2D Numpy Board that is the same size as the initialized board for the class.
        :return: None
        """

        if board.shape != self.board.shape:
            raise ValueError(f"The provide board shape: {board.shape} does not match the board size: {self.board.shape}")

        self.board = board.copy()

    def reset(self):
        """
        Resets the current board to a fresh empty board.
        :return: None
        """

        self.board = np.empty((self.board_size, self.board_size))
        self.board.fill(-1)

    def _is_complete(self, board):
        """
        Helper function to evaluate whether a provided board has been completed.
        :param board: The board to evaluate completeness for.
        :return: True if all cells are filled, False otherwise.
        """

        return np.count_nonzero(board == -1) == 0

    # STUDENT TO IMPLEMENT A CAN_PLACE.  THE SIGNATURE HERE IS A SUGGESTION, IT CAN BE MODIFIED
    def can_place(self, board, row, col, value):
        """
        Accepts a current board, and verifies if the provided value can be placed in the indicated row and column.

        :param board: The board to evaluate.  This is generally a partially complete board.
        :param row: The row of which the digit is being placed.
        :param col: The column of which the digit is being placed.
        :param value: The digit being placed in the cell.
        :return: False if there exists a matching digit in the same row, column or section.  True otherwise.
        """
        pass

    # STUDENT TO IMPLEMENT A _SOLVE.  THE SIGNATURE HERE IS A SUGGESTION, IT CAN BE MODIFIED
    def _solve(self, board):
        """
        Recursive Function to solve a provided board.
        :param board: The current iteration of the board in order to solve.
        :return: True if the board is completed/solved, False otherwise.
        """
        """
        1  2  4 |  5 6 7 | 8 8 8 |
        X  3  6 
        """

        # What row/col is next?
        row, col = self.get_next_cell(board)

        for i in range(9):
            r = self.can_place(board,row=1,col=0, 3)
            if r:
                new_board = self.board.copy()
                new_board[row][col] = i
                is_solved = self._solve(new_board)

                if is_solved:
                    return True
        pass

    # STUDENT TO IMPLEMENT (BUT CAN USE THE SAMPLE CODE AS IS BELOW)  SIGNATURE MUST REMAIN FOR SUBMISSION.
    def solve(self):
        """
        Uses the board's base as the initial board to solve recursively.
        :return: True if the board is solved, false otherwise.
        """
        return self._solve(self.board.copy())


def test_sudoku_solver():
    """
    Basic test that has a few sample board configurations pulled from known solvable solutions.
    :return:  True
    :raises: AssertionError if either test fails.
    """
    test_puzzle_easy = np.array((
        [3, 5, -1, -1, -1, 7, 2, 8, -1],
        [-1, 6, 1, -1, -1, -1, -1, -1, -1],
        [9, -1, 7, -1, 1, 4, -1, 5, -1],
        [-1, -1, 8, 4, 2, -1, -1, -1, -1],
        [-1, 3, 2, 9, -1, 5, 8, 7, -1],
        [-1, -1, -1, -1, 7, 8, 1, -1, -1],
        [-1, 2, -1, 7, 4, -1, 5, -1, 6],
        [-1, -1, -1, -1, -1, -1, 9, 4, -1],
        [-1, 9, 6, 1, -1, -1, -1, 3, 8]
    ))

    test_easy = SudokuSolver(3)
    test_easy.loader(test_puzzle_easy)

    test_easy_results = test_easy.solve()
    assert test_easy_results, "Unable to solve a solvable puzzle"
    print("Solved!")
    print(test_easy.draw_solution())

    test_puzzle_hard = np.array((
        [-1, -1, -1, 4, -1, -1, -1, -1, -1],
        [2, -1, 4, 7, -1, 1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, 5, -1, 1],
        [6, 7, -1, -1, 3, -1, 4, -1, -1],
        [-1, -1, 5, -1, -1, -1, 7, -1, -1],
        [-1, -1, 9, -1, 4, -1, -1, 2, 8],
        [1, -1, 6, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, 6, -1, 4, 8, -1, 9],
        [-1, -1, -1, -1, -1, 8, -1, -1, -1]
    ))
    test_hard = SudokuSolver(3)
    test_hard.loader(test_puzzle_hard)

    test_hard_results = test_hard.solve()
    assert test_hard_results, "Unable to solve a solvable puzzle"
    print("Solved!")
    print(test_hard.draw_solution())

    test_unsolvable_puzzle = np.array((
        [1, -1, 3, 4, 5, 6, 7, 8, 9],
        [-1, 2, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1]
    ))

    test_unsolvable = SudokuSolver(3)
    test_unsolvable.loader(test_unsolvable_puzzle)
    test_unsolvable_results = test_unsolvable.solve()
    assert not test_unsolvable_results, "Unsolvable should return false."
    print("Identified correctly as unsolvable.")
    print(test_unsolvable)


if __name__ == "__main__":
    test_sudoku_solver()
