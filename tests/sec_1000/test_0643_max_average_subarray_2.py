from unittest import TestCase, main
from tasks.sec_1000.task_0643_max_average_subarray_2 import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        r = self.s.findMaxAverage([1, 12, -5, -6, 50, 3], 4)
        self.assertEqual(12.75, r)

    def test02(self):
        r = self.s.findMaxAverage([5], 1)
        self.assertEqual(5.00, r)

    def test03(self):
        r = self.s.findMaxAverage([-1], 1)
        self.assertEqual(-1.00, r)


if __name__ == '__main__':
    main()
