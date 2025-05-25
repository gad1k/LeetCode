from unittest import TestCase, main
from tasks.sec_0500.task_0189_rotate_array import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        self.s.rotate(nums, 3)
        self.assertListEqual([5, 6, 7, 1, 2, 3, 4], nums)

    def test02(self):
        nums = [-1, -100, 3, 99]
        self.s.rotate(nums, 2)
        self.assertListEqual([3, 99, -1, -100], nums)


if __name__ == '__main__':
    main()
