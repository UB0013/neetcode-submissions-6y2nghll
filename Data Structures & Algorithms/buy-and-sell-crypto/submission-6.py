class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minbuy = prices[0]
        profit = 0 

        for cost in prices:
            minbuy = min (minbuy,cost)
            profit = max(profit, cost-minbuy)
        return profit

        