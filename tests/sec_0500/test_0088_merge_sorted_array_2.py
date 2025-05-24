from unittest import TestCase, main
from tasks.sec_0500.task_0088_merge_sorted_array_2 import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        nums2 = [2, 5, 6]
        self.s.merge(nums1, 3, nums2, 3)
        self.assertListEqual(nums1, [1, 2, 2, 3, 5, 6])

    def test02(self):
        nums1 = [1]
        nums2 = []
        self.s.merge(nums1, 1, nums2, 0)
        self.assertListEqual(nums1, [1])

    def test03(self):
        nums1 = [0]
        nums2 = [1]
        self.s.merge(nums1, 0, nums2, 1)
        self.assertListEqual(nums1, [1])

    def test04(self):
        nums1 = [2, 0]
        nums2 = [1]
        self.s.merge(nums1, 1, nums2, 1)
        self.assertListEqual(nums1, [1, 2])

    def test05(self):
        nums1 = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
        nums2 = [1, 2, 2]
        self.s.merge(nums1, 6, nums2, 3)
        self.assertListEqual(nums1, [-1, 0, 0, 1, 2, 2, 3, 3, 3])

    def test06(self):
        nums1 = [4, 0, 0, 0, 0, 0]
        nums2 = [1, 2, 3, 5, 6]
        self.s.merge(nums1, 1, nums2, 5)
        self.assertListEqual(nums1, [1, 2, 3, 4, 5, 6])


if __name__ == '__main__':
    main()
