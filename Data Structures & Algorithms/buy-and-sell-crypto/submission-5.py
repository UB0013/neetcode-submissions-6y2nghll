class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy = 0 
        # sell = 0 
        # profit = 0 
        # for i in range (len(prices)-1, -1 , -1):
        #     sell = prices[i]
        #     while i-1 >= 0 : 
        #         buy = min (buy, prices[i])
        #     i = i-1 
        #     profit = max(profit, (buy - sell))

        # return max(profit,0)
        buy =prices[0]
        sell = 0 
        profit= 0 

        for price in prices : 
            buy = min (buy,price)
            sell = price
            profit = max(profit, sell-buy )
        return profit 


        