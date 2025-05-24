from unittest import TestCase, main
from tasks.sec_1000.task_0977_squares_of_a_sorted_array import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        self.assertListEqual(self.s.sortedSquares([-4, -1, 0, 3, 10]), [0, 1, 9, 16, 100])

    def test02(self):
        self.assertListEqual(self.s.sortedSquares([-7, -3, 2, 3, 11]), [4, 9, 9, 49, 121])


if __name__ == '__main__':
    main()
