class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

# dp[j] still holds the value from the ROW BELOW because we haven't overwritten it yet
# Iterating right→left makes dp[j+1] already updated, so it represents the RIGHT cell
# dp[j] += dp[j+1] correctly means paths = from below + from right (even though moves are down/right)

        dp = [1] * n 

        for r in range(m-2,-1,-1):
            for j in range (n-2,-1,-1) : 
                dp[j] = dp[j] + dp [j+1]
        return dp[0]
            

        