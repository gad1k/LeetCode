class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        return sorted([num * num for num in nums])
