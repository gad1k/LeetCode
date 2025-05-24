class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        total_profit = 0
        for i in range(len(prices)-1):
            total_profit += max((prices[i+1]-prices[i]), 0)

        return total_profit
