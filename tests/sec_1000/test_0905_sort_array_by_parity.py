from unittest import TestCase, main
from tasks.sec_1000.task_0905_sort_array_by_parity import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        nums = [3, 1, 2, 4]
        self.s.sortArrayByParity(nums)
        self.assertListEqual([2, 4, 3, 1], nums)

    def test02(self):
        nums = [0]
        self.s.sortArrayByParity(nums)
        self.assertListEqual([0], nums)

    def test03(self):
        nums = [3, 1]
        self.s.sortArrayByParity(nums)
        self.assertListEqual([3, 1], nums)


if __name__ == '__main__':
    main()
