from unittest import TestCase, main
from tasks.sec_0500.task_0026_remove_duplicates_from_sorted_array import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        nums = [1, 1, 2]
        k = self.s.removeDuplicates(nums)
        self.assertEqual(k, 2)
        self.assertListEqual(nums, [1, 2, 2])

    def test02(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        k = self.s.removeDuplicates(nums)
        self.assertEqual(k, 5)
        self.assertListEqual(nums, [0, 1, 2, 3, 4, 2, 2, 3, 3, 4])


if __name__ == '__main__':
    main()
