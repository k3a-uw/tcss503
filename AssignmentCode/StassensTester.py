# MAKE SURE YOUR SUBMISSION IS NAMED Strassens.py to ensure tests will work properly.
from Strassens import strassens
import numpy as np

class StassensTester:

    def __init__(self, strassens):
        self.student_strassens = strassens
        self.results = []
        N = 16
        self.tests = [
            {
                "name": "1.1 Empty Matrices as Input",
                "A": [[]],
                "B": [[]],
                "expected": [[]]
            },
            {
                "name": "1.2 Easy 2x2 Matrices as Input",
                "A": [[1, 1],
                      [0, 0]],
                "B": [[2, 3],
                      [4, 10]],
                "expected": np.array([[6, 13],
                                      [0, 0]])
            },
            {
                "name": "1.3 Medium 3x3 Matrices as Input",
                "A": [[1, 2, 3, 4],
                      [5, 6, 7, 8],
                      [9, 10, 11, 12],
                      [13, 14, 15, 16]],
                "B": [[1, 2, 3, 4],
                      [5, 6, 7, 8],
                      [9, 10, 11, 12],
                      [13, 14, 15, 16]],
                "expected": np.array([[90, 100, 110, 120],
                                      [202, 228, 254, 280],
                                      [314, 356, 398, 440],
                                      [426, 484, 542, 600]])
            },
            {
                "name": "1.4 Large 3x3 Matrices as Input",
                "A": [[-10, 20, 30, 40, 50, 60, 70, -80],
                      [10, -20, 30, 40, 50, 60, -70, 80],
                      [10, 20, -30, 40, 50, -60, 70, 80],
                      [10, 20, 30, -40, -50, 60, 70, 80],
                      [10, 20, 30, -40, -50, 60, 70, 80],
                      [10, 20, -30, 40, 50, -60, 70, 80],
                      [10, -20, 30, 40, 50, 60, -70, 80],
                      [-10, 20, 30, 40, 50, 60, 70, -80]],
                "B": [[-1, 1, 1, 1, 1, 1, 1, -1],
                      [1, -1, 1, 1, 1, 1, -1, 1],
                      [1, 1, -1, 1, 1, -1, 1, 1],
                      [1, 1, 1, -1, -1, 1, 1, 1],
                      [1, 1, 1, -1, -1, 1, 1, 1],
                      [1, 1, -1, 1, 1, -1, 1, 1],
                      [1, -1, 1, 1, 1, 1, -1, 1],
                      [-1, 1, 1, 1, 1, 1, 1, -1]],
                "expected": np.array([[360, 0, 0, 0, 0, 0, 0, 360],
                                      [0, 360, 0, 0, 0, 0, 360, 0],
                                      [0, 0, 360, 0, 0, 360, 0, 0],
                                      [0, 0, 0, 360, 360, 0, 0, 0],
                                      [0, 0, 0, 360, 360, 0, 0, 0],
                                      [0, 0, 360, 0, 0, 360, 0, 0],
                                      [0, 360, 0, 0, 0, 0, 360, 0],
                                      [360, 0, 0, 0, 0, 0, 0, 360]])
            },
            {
                "name": "1.5 Massive 50x50 Matrices as Input",
                "A": np.fromfunction(lambda i, j: i * N + j + 1, (N, N), dtype=int),
                "B": np.fromfunction(lambda i, j: i * N + j + 1, (N, N), dtype=int),
                "expected": np.array([ [ 21896,  22032,  22168,  22304,  22440,  22576,  22712,  22848,
                                         22984,  23120,  23256,  23392,  23528,  23664,  23800,  23936],
                                       [ 52872,  53264,  53656,  54048,  54440,  54832,  55224,  55616,
                                         56008,  56400,  56792,  57184,  57576,  57968,  58360,  58752],
                                       [ 83848,  84496,  85144,  85792,  86440,  87088,  87736,  88384,
                                         89032,  89680,  90328,  90976,  91624,  92272,  92920,  93568],
                                       [114824, 115728, 116632, 117536, 118440, 119344, 120248, 121152,
                                        122056, 122960, 123864, 124768, 125672, 126576, 127480, 128384],
                                       [145800, 146960, 148120, 149280, 150440, 151600, 152760, 153920,
                                        155080, 156240, 157400, 158560, 159720, 160880, 162040, 163200],
                                       [176776, 178192, 179608, 181024, 182440, 183856, 185272, 186688,
                                        188104, 189520, 190936, 192352, 193768, 195184, 196600, 198016],
                                       [207752, 209424, 211096, 212768, 214440, 216112, 217784, 219456,
                                        221128, 222800, 224472, 226144, 227816, 229488, 231160, 232832],
                                       [238728, 240656, 242584, 244512, 246440, 248368, 250296, 252224,
                                        254152, 256080, 258008, 259936, 261864, 263792, 265720, 267648],
                                       [269704, 271888, 274072, 276256, 278440, 280624, 282808, 284992,
                                        287176, 289360, 291544, 293728, 295912, 298096, 300280, 302464],
                                       [300680, 303120, 305560, 308000, 310440, 312880, 315320, 317760,
                                        320200, 322640, 325080, 327520, 329960, 332400, 334840, 337280],
                                       [331656, 334352, 337048, 339744, 342440, 345136, 347832, 350528,
                                        353224, 355920, 358616, 361312, 364008, 366704, 369400, 372096],
                                       [362632, 365584, 368536, 371488, 374440, 377392, 380344, 383296,
                                        386248, 389200, 392152, 395104, 398056, 401008, 403960, 406912],
                                       [393608, 396816, 400024, 403232, 406440, 409648, 412856, 416064,
                                        419272, 422480, 425688, 428896, 432104, 435312, 438520, 441728],
                                       [424584, 428048, 431512, 434976, 438440, 441904, 445368, 448832,
                                        452296, 455760, 459224, 462688, 466152, 469616, 473080, 476544],
                                       [455560, 459280, 463000, 466720, 470440, 474160, 477880, 481600,
                                        485320, 489040, 492760, 496480, 500200, 503920, 507640, 511360],
                                       [486536, 490512, 494488, 498464, 502440, 506416, 510392, 514368,
                                        518344, 522320, 526296, 530272, 534248, 538224, 542200, 546176]])
            }
        ]

    def assert_condition(self, test_title, condition, failure_message, possible_points=1, penalty=-1):
        """Helper function to log test results"""
        if condition:
            self.results.append((test_title, True, 'Successful', possible_points, 0))
        else:
            self.results.append((test_title, False, failure_message, possible_points, penalty))

    def first_test_empty_maxtrices(self):
        A = np.array([[]])
        B = np.array([[]])
        expected_val = np.array([[]])
        x = self.student_strassens(A, B)
        self.assert_condition("1.1 Empty Matrices as Input", np.array_equal(expected_val, x), "Did not receive an empty matrix.", 5, -5)

    def run_tests(self):
        """Run all test cases"""
        self.results.clear()
        for t in self.tests:
            print("Testing " + t["name"])
            result = self.student_strassens(t['A'],t['B'])
            self.assert_condition(t['name'], np.array_equal(result, t['expected']),'Invalid Result',5,-5)


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
    test = StassensTester(strassens)

    test.run_tests()
    test.print_results()