from unittest import TestCase, main
from tasks.sec_0500.task_0448_find_disappeared_numbers import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        nums = [4, 3, 2, 7, 8, 2, 3, 1]
        r = self.s.findDisappearedNumbers(nums)
        self.assertListEqual([5, 6], r)

    def test02(self):
        nums = [1, 1]
        r = self.s.findDisappearedNumbers(nums)
        self.assertListEqual([2], r)


if __name__ == '__main__':
    main()
