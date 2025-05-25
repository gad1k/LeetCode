from unittest import TestCase, main
from tasks.sec_1500.task_1480_running_sum_of_1d_array import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        r = self.s.runningSum([1, 2, 3, 4])
        self.assertListEqual([1, 3, 6, 10], r)

    def test02(self):
        r = self.s.runningSum([1, 1, 1, 1, 1])
        self.assertListEqual([1, 2, 3, 4, 5], r)

    def test03(self):
        r = self.s.runningSum([3, 1, 2, 10, 1])
        self.assertListEqual([3, 4, 6, 16, 17], r)


if __name__ == '__main__':
    main()
