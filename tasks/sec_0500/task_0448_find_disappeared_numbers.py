class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        disappearedNums = list()
        distinctNums = set(nums)

        for i in range(1, len(nums) + 1):
            if i not in distinctNums:
                disappearedNums.append(i)

        return disappearedNums
