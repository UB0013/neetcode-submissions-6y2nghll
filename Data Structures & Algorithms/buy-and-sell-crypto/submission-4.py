class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l =0 
        r = 1
        res = 0 
        profit =0
        while r < len(prices):
            profit = prices[r]-prices[l]
            res = max(res,profit)
            if prices[r] < prices[l] : 
                l = r 
            r = r+1 
        
        return res

        