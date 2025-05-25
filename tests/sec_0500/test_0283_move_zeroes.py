from unittest import TestCase, main
from tasks.sec_0500.task_0283_move_zeroes import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        nums = [0, 1, 0, 3, 12]
        self.s.moveZeroes(nums)
        self.assertListEqual([1, 3, 12, 0, 0], nums)

    def test02(self):
        nums = [0]
        self.s.moveZeroes(nums)
        self.assertListEqual([0], nums)

    def test03(self):
        nums = [2, 1]
        self.s.moveZeroes(nums)
        self.assertListEqual([2, 1], nums)

    def test04(self):
        nums = [1, 0, 1]
        self.s.moveZeroes(nums)
        self.assertListEqual([1, 1, 0], nums)

    def test05(self):
        nums = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
        self.s.moveZeroes(nums)
        self.assertListEqual([4, 2, 4, 3, 5, 1, 0, 0, 0, 0], nums)


if __name__ == '__main__':
    main()
