class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        totalProfit = 0
        for i in range(len(prices)-1):
            totalProfit += max((prices[i+1]-prices[i]), 0)

        return totalProfit
