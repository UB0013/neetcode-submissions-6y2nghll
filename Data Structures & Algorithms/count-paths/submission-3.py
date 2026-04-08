class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # dp[j] always represents paths from the cell BELOW; when iterating right→left, dp[j+1] is already the RIGHT cell
# We build paths backwards (destination → start): paths = from right + from below, even though moves are right/down
# Initializing row/newRow with 1s auto-handles the last column (only one way: move down)

        prevrow = [1] * n 

        for i in range(m-1):
            newrow = [1] * n 
            for j in range (n-2,-1,-1):
                newrow[j] = prevrow[j] + newrow[j+1]
            
            prevrow =newrow 
        return prevrow[0]

        