from unittest import TestCase, main
from tasks.sec_0500.task_0027_remove_element import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        nums = [3, 2, 2, 3]
        k = self.s.removeElement(nums, 3)
        self.assertEqual(2, k)
        self.assertListEqual([2, 2, 3, 3], nums)

    def test02(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        k = self.s.removeElement(nums, 2)
        self.assertEqual(5, k)
        self.assertListEqual([0, 1, 4, 0, 3, 2, 2, 2], nums)


if __name__ == '__main__':
    main()
