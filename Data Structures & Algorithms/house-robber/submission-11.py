class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len (nums)
        dp = {}
        def dfs (i) : 
            if i in dp :
                return dp[i]
            if i >= n :
                return 0 
            dp [i] = max (nums[i] + dfs(i+2), nums[i]+ dfs (i+3))
            return dp[i]

        
        return max (dfs (0), dfs (1)) 
        