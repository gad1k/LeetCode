from unittest import TestCase, main
from tasks.sec_0500.task_0283_move_zeroes import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        nums = [0, 1, 0, 3, 12]
        self.s.moveZeroes(nums)
        self.assertListEqual(nums, [1, 3, 12, 0, 0])

    def test02(self):
        nums = [0]
        self.s.moveZeroes(nums)
        self.assertListEqual(nums, [0])

    def test03(self):
        nums = [2, 1]
        self.s.moveZeroes(nums)
        self.assertListEqual(nums, [2, 1])

    def test04(self):
        nums = [1, 0, 1]
        self.s.moveZeroes(nums)
        self.assertListEqual(nums, [1, 1, 0])

    def test05(self):
        nums = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
        self.s.moveZeroes(nums)
        self.assertListEqual(nums, [4, 2, 4, 3, 5, 1, 0, 0, 0, 0])


if __name__ == '__main__':
    main()
