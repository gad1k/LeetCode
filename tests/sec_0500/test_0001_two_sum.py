from unittest import TestCase, main
from tasks.sec_0500.task_0001_two_sum import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        r = self.s.twoSum([2, 7, 11, 15], 9)
        self.assertListEqual([0, 1], r)

    def test02(self):
        r = self.s.twoSum([3, 2, 4], 6)
        self.assertListEqual([1, 2], r)

    def test03(self):
        r = self.s.twoSum([3, 3], 6)
        self.assertListEqual([0, 1], r)


if __name__ == '__main__':
    main()
