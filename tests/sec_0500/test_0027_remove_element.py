from unittest import TestCase, main
from tasks.sec_0500.task_0027_remove_element import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        nums = [3, 2, 2, 3]
        k = self.s.removeElement(nums, 3)
        self.assertEqual(k, 2)
        self.assertListEqual(nums, [2, 2, 3, 3])

    def test02(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        k = self.s.removeElement(nums, 2)
        self.assertEqual(k, 5)
        self.assertListEqual(nums, [0, 1, 4, 0, 3, 2, 2, 2])


if __name__ == '__main__':
    main()
