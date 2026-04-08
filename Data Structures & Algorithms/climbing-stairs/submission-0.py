class Solution:
    def climbStairs(self, n: int) -> int:

        dp = (n+1) * [0]

        dp[0] = 1
        dp[1] = 1
        i = 2 
        for i in range (2,len(dp)):
            dp [i] = dp [i-1]+ dp [i-2]
        
        return dp[n]
        