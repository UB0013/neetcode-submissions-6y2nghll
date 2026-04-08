"""dp[i] = minimum cost to reach step i
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len (cost)
        dp = [0] * (n+1)
        
        dp[0] = 0 
        dp [1] = cost[0] 

        #  0   1       2           3   
        #  0   1       2           4 

        #dp[] = 0 , 1 

        for i in range (2,n+1):
            dp [i] =  cost [i-1]+ (min ( dp[i-1], dp[i-2]))
            
        
        return min ( dp[n-1], dp[n]) 

       