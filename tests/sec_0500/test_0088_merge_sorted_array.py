from unittest import TestCase, main
from tasks.sec_0500.task_0088_merge_sorted_array import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        nums2 = [2, 5, 6]
        self.s.merge(nums1, 3, nums2, 3)
        self.assertListEqual([1, 2, 2, 3, 5, 6], nums1)

    def test02(self):
        nums1 = [1]
        nums2 = []
        self.s.merge(nums1, 1, nums2, 0)
        self.assertListEqual([1], nums1)

    def test03(self):
        nums1 = [0]
        nums2 = [1]
        self.s.merge(nums1, 0, nums2, 1)
        self.assertListEqual([1], nums1)


if __name__ == '__main__':
    main()
