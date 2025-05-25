class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        upperBound, i, j = m, 0, 0
        while i < upperBound:
            if j < n and nums1[i] >= nums2[j]:
                nums1.insert(i, nums2[j])
                upperBound += 1
                j += 1
            else:
                i += 1

        nums1[:] = nums1[:upperBound]
        if i == upperBound and j < n:
            nums1[:] = nums1 + nums2[j:]
