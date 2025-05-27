from unittest import TestCase, main
from tasks.sec_0500.task_0031_next_permutation import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        nums = [1, 2, 3]
        self.s.nextPermutation(nums)
        self.assertListEqual([1, 3, 2], nums)

    def test02(self):
        nums = [3, 2, 1]
        self.s.nextPermutation(nums)
        self.assertListEqual([1, 2, 3], nums)

    def test03(self):
        nums = [1, 1, 5]
        self.s.nextPermutation(nums)
        self.assertListEqual([1, 5, 1], nums)

    def test04(self):
        nums = [1, 3, 2]
        self.s.nextPermutation(nums)
        self.assertListEqual([2, 1, 3], nums)

    def test05(self):
        nums = [1, 1]
        self.s.nextPermutation(nums)
        self.assertListEqual([1, 1], nums)


if __name__ == '__main__':
    main()
