class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        l= 0 
        r = 0 
        profit = 0 
        max_profit  =0 
        buy  = prices [l]
        for r in  range ( len (prices)): 
            profit  = prices[r]- buy 
            print (profit)
            max_profit = max(max_profit, profit)
            if prices[r] < buy :
                buy = prices[r]
            #r = r+1 
            
        return max_profit 
        