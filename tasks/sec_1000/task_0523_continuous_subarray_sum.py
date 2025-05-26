class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        mods = {0: -1}
        total = 0

        for i in range(len(nums)):
            total += nums[i]
            mod = total % k
            if mod in mods:
                if i - mods.get(mod) >= 2:
                    return True
            else:
                mods[mod] = i

        return False
