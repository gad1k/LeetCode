class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        slow = 0

        for fast in range(1, len(nums)):
            if nums[fast] != nums[fast - 1]:
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1
