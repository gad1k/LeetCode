class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hits = dict()

        for i, num in enumerate(nums):
            complement = target - num
            if complement in hits:
                return [hits[complement], i]
            hits[num] = i

        return []
