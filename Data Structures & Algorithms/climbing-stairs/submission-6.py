class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 :
            return 0 
        dp = [-1]*n 
        def dfs (steps) : 
            if steps == n :
                return 1 
            if steps > n : 
                return 0
            if dp[steps] != -1 :
                return dp[steps]
            if steps < n :
                dp[steps] = dfs (steps + 1) + dfs (steps +2)
                return dp[steps]
            
        return dfs (0)
            

        