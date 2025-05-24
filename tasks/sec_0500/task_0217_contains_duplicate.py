class Solution:
    def containsDuplicates(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))
