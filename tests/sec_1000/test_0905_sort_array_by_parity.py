from unittest import TestCase, main
from tasks.sec_1000.task_0905_sort_array_by_parity import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        nums = [3, 1, 2, 4]
        self.s.sortArrayByParity(nums)
        self.assertListEqual(nums, [2, 4, 3, 1])

    def test02(self):
        nums = [0]
        self.s.sortArrayByParity(nums)
        self.assertListEqual(nums, [0])

    def test03(self):
        nums = [3, 1]
        self.s.sortArrayByParity(nums)
        self.assertListEqual(nums, [3, 1])


if __name__ == '__main__':
    main()
