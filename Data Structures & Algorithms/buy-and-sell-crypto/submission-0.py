class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for sell in prices:
            buy = min(buy, sell)
            profit = max(sell - buy, profit)
        return profit
