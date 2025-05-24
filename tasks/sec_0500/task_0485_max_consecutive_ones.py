class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        cntCur = 0
        cntMax = 0

        for num in nums:
            if num == 1:
                cntCur += 1
            else:
                cntMax = max(cntMax, cntCur)
                cntCur = 0

        return max(cntMax, cntCur)
