class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = float("inf")
        l = 0 
        r =0 
        summ = 0 
        while r < len(nums)  : 
            summ += nums[r] 
            while summ >= target : 
                result = min (result , r-l+1) 
                summ -= nums[l]
                l = l +1
            r = r +1 
        return result if result !=  float("inf") else 0 











        min ( result,window)
        