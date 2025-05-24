class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        sortedNums = sorted(set(nums), reverse=True)

        if len(sortedNums) >= 3:
            return sortedNums[2]
        else:
            return sortedNums[0]
