class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = set (nums)
        
        count = 1 
        res = 0 

        for i in range ( len (nums)) : 
            if nums[i] - 1  not in arr : 
                count =1 
                while nums[i] + count in arr : 
                    count = count +1 
                
            res = max(res,count )
        return res 

        

        





   

        

        
        