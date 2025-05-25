from unittest import TestCase, main
from tasks.sec_0500.task_0349_intersection_of_two_arrays import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        r = self.s.intersection([1, 2, 2, 1], [2, 2])
        self.assertListEqual([2], r)

    def test02(self):
        r = self.s.intersection([4, 9, 5], [9, 4, 9, 8, 4])
        self.assertListEqual([9, 4], r)


if __name__ == '__main__':
    main()
