from unittest import TestCase, main
from tasks.sec_0500.task_0056_merge_intervals import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        r = self.s.merge(intervals)
        self.assertEqual([[1, 6], [8, 10], [15, 18]], r)

    def test02(self):
        intervals = [[1, 4], [4, 5]]
        r = self.s.merge(intervals)
        self.assertListEqual([[1, 5]], r)

    def test03(self):
        intervals = [[1, 4], [0, 4]]
        r = self.s.merge(intervals)
        self.assertListEqual([[0, 4]], r)


if __name__ == '__main__':
    main()
