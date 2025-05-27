from unittest import TestCase, main
from tasks.sec_1000.task_0986_interval_list_intersection import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        first = [[0, 2], [5, 10], [13, 23], [24, 25]]
        second = [[1, 5], [8, 12], [15, 24], [25, 26]]
        r = self.s.intervalIntersection(first, second)
        self.assertListEqual([[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]], r)

    def test02(self):
        first = [[1, 3], [5, 9]]
        second = []
        r = self.s.intervalIntersection(first, second)
        self.assertListEqual([], r)


if __name__ == '__main__':
    main()
