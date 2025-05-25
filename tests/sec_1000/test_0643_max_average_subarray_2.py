from unittest import TestCase, main
from tasks.sec_1000.task_0643_max_average_subarray_2 import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        result = self.s.findMaxAverage([1, 12, -5, -6, 50, 3], 4)
        self.assertEqual(result, 12.75)

    def test02(self):
        result = self.s.findMaxAverage([5], 1)
        self.assertEqual(result, 5.00)

    def test03(self):
        result = self.s.findMaxAverage([-1], 1)
        self.assertEqual(result, -1.00)


if __name__ == '__main__':
    main()
