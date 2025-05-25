from unittest import TestCase, main
from tasks.sec_1000.task_0977_squares_of_a_sorted_array import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        r = self.s.sortedSquares([-4, -1, 0, 3, 10])
        self.assertListEqual([0, 1, 9, 16, 100], r)

    def test02(self):
        r = self.s.sortedSquares([-7, -3, 2, 3, 11])
        self.assertListEqual([4, 9, 9, 49, 121], r)


if __name__ == '__main__':
    main()
