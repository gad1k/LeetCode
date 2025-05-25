from unittest import TestCase, main
from tasks.sec_0500.task_0026_remove_duplicates_from_sorted_array import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        nums = [1, 1, 2]
        k = self.s.removeDuplicates(nums)
        self.assertEqual(2, k)
        self.assertListEqual([1, 2, 2], nums)

    def test02(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        k = self.s.removeDuplicates(nums)
        self.assertEqual(5, k)
        self.assertListEqual([0, 1, 2, 3, 4, 2, 2, 3, 3, 4], nums)


if __name__ == '__main__':
    main()
