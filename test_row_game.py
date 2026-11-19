import unittest

from row_game import solution


class SolutionTests(unittest.TestCase):
    def test_repeat_single_positive_cell(self):
        self.assertEqual(solution([3], 4), 12)

    def test_no_affordable_first_move(self):
        self.assertEqual(solution([-8, 2], 7), 0)

    def test_zero_turns(self):
        self.assertEqual(solution([2, 3], 0), 0)

    def test_large_turn_budget(self):
        self.assertEqual(solution([1, 2], 100_000_000), 300_000_000)


if __name__ == '__main__':
    unittest.main()
