class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)
        def dfs (steps) : 
            if steps == 0 :
                return 1
            if steps < 0 :
                return 0
            if dp[steps] != -1 :
                return dp[steps]
            dp[steps] = dfs (steps -1) + dfs (steps - 2)
            return dp[steps]
            
        return dfs (n)
            

        