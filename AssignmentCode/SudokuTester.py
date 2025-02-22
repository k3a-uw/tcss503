import numpy as np
import SudokuSolver

class SudokuTester:

    def __init__(self, solver):
        self.student_solver = solver
        self.results = []



    def assert_condition(self, test_title, condition, failure_message, possible_points=1, penalty=-1):
        """Helper function to log test results"""
        if condition:
            self.results.append((test_title, True, 'Successful', possible_points, 0))
        else:
            self.results.append((test_title, False, failure_message, possible_points, penalty))

    def run_tests(self):
        """Run all test cases"""

        self.results.clear()

        ss = self.test_structure()
        ss = self.test_loader(ss)
        if ss:
            ss = self.test_can_place(ss)
        if ss:
            ss = self.test_solve(ss)

        if not ss:
            print("Failure to run all test cases.  Look closely at your results.")

    def test_structure(self):
        try:
            ss = self.student_solver.SudokuSolver(3)
        except NameError:
            self.results.append(('0.*: All Pre-Tests Failed.', False, "SudokuSolver class is Not defined", 50, -50))
            return
        except Exception as e:
            self.results.append(('0.*: All Pre-Tests Failed.', False, f"Error during instantiation: {e}", 50, -50))
            return
        else:
            self.assert_condition('0.1 SudokuSolver Class Exists', True, '', 2, -2)
            self.assert_condition('0.2 SudokuSolver Can be instantiated.', True, '', 1, -1)

        self.assert_condition('0.3 solve method exists', hasattr(ss, 'solve') and callable(getattr(ss, 'solve', None)), 'solve method is missing or not callable.', 1,-1)
        self.assert_condition('0.4 can_place method exists', hasattr(ss, 'can_place') and callable(getattr(ss, 'can_place', None)), 'can_place method is missing or not callable.', 1,-1)

        return ss

    def test_loader(self, ss):
        board = np.zeros((9, 9), dtype=int)
        board2 = np.ones((9, 9), dtype=int)
        try:
            ss.loader(board)
        except Exception as e:
            self.results.append(('1.*: Loader Tests Failed',False, f"Error during exeucuting Loader {e}", 45, -45))

        self.assert_condition("1.1 Loaded Board Should Equal self.board", (ss.board == board).all(), 'Boards do not match', 4, -4)

        try:
            ss.loader(board2)
        except Exception as e:
            self.results.append('1.2 Loader can be executed with a second board.',False, f"Error during exeucuting Loader {e}", 3, -3)
        else:
            self.assert_condition("1.2 Loader can be executed with a second board.", (ss.board == board2).all(), '2nd Board Not Saved', 1, -1)

        return ss

    def test_can_place(self,ss):

        x = np.array((
            [1, 2, 3, 4, 5, 6, 7, 8, -1],
            [-1, 5, 6, 7, 8, 9, 1, 2, 3],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1],
            [9, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        ))

        # TEST PLACE IN ROW 0, COL 8 THE VALUE 1 SHOULD BE FALSE
        # TEST PLACE IN ROW 0, COL 8 THE VALUE 9 SHOULD BE TRUE
        self.assert_condition('2.1 Test Negative Row Check for Can_place', not ss.can_place(x, 0, 8, 1), 'Invalid check for row placement', 5, -5)
        self.assert_condition('2.2 Test Positive Row Check for Can_place', ss.can_place(x, 0, 8, 9),'Invalid check for row placement', 2.5, -2.5)

        # TEST PLACE IN ROW 1, COL 1 THE VALUE 9 SHOULD BE FALSE
        # TEST PLACE IN ROW 1, COL 1 THE VALUE 4 SHOULD BE TRUE
        self.assert_condition('2.3 Test Negative Col Check for Can_place', not ss.can_place(x, 1, 1, 9), 'Invalid check for col placement', 5, -5)
        self.assert_condition('2.4 Test Positive Col Check for Can_place', ss.can_place(x, 1, 1, 4),'Invalid check for col placement', 2.5, -2.5)

        # TEST PLACE IN ROW 2, COL 1 THE VALUE 5 SHOULD BE FALSE
        # TEST PLACE IN ROW 2, COL 1 THE VALUE 4 SHOULD BE TRUE
        self.assert_condition('2.5 Test Negative Cell Check for Can_place', not ss.can_place(x, 2, 1, 5), 'Invalid check for cell placement', 5, -5)
        self.assert_condition('2.6 Test Positive Cell Check for Can_place', ss.can_place(x, 2, 1, 4),'Invalid check for cell placement', 5, -5)

        return ss

    def test_solve(self, ss):

        # THREE TESTS, THE EASY PUZZLE, THE HARD PUZZLE AND THE UNSOLVABLE PUZZLE.
        easy = np.array((
                    [3, 5, -1, -1, -1, 7, 2, 8, -1],
                    [-1, 6, 1, -1, -1, -1, -1, -1, -1],
                    [9, -1, 7, -1, 1, 4, -1, 5, -1],
                    [-1, -1, 8, 4, 2, -1, -1, -1, -1],
                    [-1, 3, 2, 9, -1, 5, 8, 7, -1],
                    [-1, -1, -1, -1, 7, 8, 1, -1, -1],
                    [-1, 2, -1, 7, 4, -1, 5, -1, 6],
                    [-1, -1, -1, -1, -1, -1, 9, 4, -1],
                    [-1, 9, 6, 1, -1, -1, -1, 3, 8]))

        hard = np.array((
                    [-1, -1, -1, 4, -1, -1, -1, -1, -1],
                    [2, -1, 4, 7, -1, 1, -1, -1, -1],
                    [-1, -1, -1, -1, -1, -1, 5, -1, 1],
                    [6, 7, -1, -1, 3, -1, 4, -1, -1],
                    [-1, -1, 5, -1, -1, -1, 7, -1, -1],
                    [-1, -1, 9, -1, 4, -1, -1, 2, 8],
                    [1, -1, 6, -1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, 6, -1, 4, 8, -1, 9],
                    [-1, -1, -1, -1, -1, 8, -1, -1, -1]))

        unsolvable = np.array((
                    [1, -1, 3, 4, 5, 6, 7, 8, 9],
                    [-1, 2, -1, -1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1, -1, -1, -1, -1]))

        try:
            ss.loader(easy)
            result = ss.solve()
            self.assert_condition(f"3.1 Solve Easy Puzzle", result, "Easy Puzzle Solve Failed", 5, -5)
        except Exception as e:
            self.results.append(("3.1. Solve Easy Puzzle", False, f"Exception {e}", 5, -5))

        try:
            ss.loader(hard)
            result = ss.solve()
            self.assert_condition(f"3.1 Solve Hard Puzzle", result, "Hard Puzzle Solver Failed", 5, -5)
        except Exception as e:
            self.results.append(("3.1. Solve Hard Puzzle", False, f"Exception {e}", 5, -5))

        try:
            ss.loader(unsolvable)
            result = ss.solve()
            self.assert_condition(f"3.1 Try Unsolvable Puzzle", not result,"Hard Puzzle Solver Failed", 5, -5)
        except Exception as e:
            self.results.append(("3.1. Solve Hard Puzzle", False, f"Exception {e}", 5, -5))

        return ss


    def print_results(self):
            if not self.results:
                print("The tests have not yet been run, please make sure to run .run_tests() before printing results.")
                return


            max_test_name = max([len(x[0]) for x in self.results])
            max_result_text = max([len(x[2]) for x in self.results])

            column_widths = [max_test_name + 2, 8, 16, max_result_text + 3]
            column_names = ['TEST NAME', 'RESULT', 'PE/PP', 'NOTE']
            header = f"{column_names[0].ljust(column_widths[0])}{column_names[1].ljust(column_widths[1])} {column_names[2].ljust(column_widths[2])}{column_names[3].ljust(column_widths[3])}"

            print(header)
            print(f"{'-' * sum(column_widths)}")

            total_possible = 0
            total_penalties = 0
            for result in self.results:
                total_possible += result[3]
                total_penalties += result[4]
                points_earned = result[3] + result[4]

                test_name_padded = result[0].ljust(column_widths[0])
                result_text = 'PASSED' if result[1] else 'FAILED'
                result_padded = result_text.ljust(column_widths[1])
                penalty_text = "" if result[4] == 0 else f"({result[4]} pts)"
                points_padded = f"{points_earned}/{result[3]} {penalty_text}".ljust(column_widths[2])
                notes_padded = f"{result[2].ljust(column_widths[3])}"

                print(f"{test_name_padded}{result_padded} {points_padded}{notes_padded}")

            total_points = total_possible + total_penalties
            print(f"{'-' * sum(column_widths)}")
            print(f"{'Points Earned (PE) / Points Possible (PP)  '.rjust(sum(column_widths[:-2]))} {total_points}/{total_possible} ({total_points*100/total_possible}%)")


if __name__ == '__main__':
    tester = SudokuTester(SudokuSolver)
    tester.run_tests()
    tester.print_results()