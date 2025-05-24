class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                for j in range(i + 1, len(nums)):
                    if nums[j] % 2 == 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
        return nums
