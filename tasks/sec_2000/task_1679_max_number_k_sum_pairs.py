class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        pairCnt = 0
        pairs = dict()

        for i in nums:
            if pairs.get(k - i, 0) == 0:
                pairs[i] = pairs.get(i, 0) + 1
            else:
                pairs[k - i] -= 1
                pairCnt += 1

        return pairCnt
