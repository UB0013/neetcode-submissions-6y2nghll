class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        currmin = 1
        currmax = 1 
        res = nums[0]

        for n in nums :
            if n == 0 :
                currmin =1 
                currmax =1 
            temp = currmin 
            currmin = min(currmax *n , currmin*n,n)
            currmax = max(currmax *n , temp*n, n)

            res = max(res,currmax)
        return res 

    