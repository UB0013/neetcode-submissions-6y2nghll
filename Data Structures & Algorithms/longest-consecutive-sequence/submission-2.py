class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums =sorted(nums)
        result =1 
        i = 0 
        count =1 
        print( sorted(nums))

        if not nums:
            return 0
        
        while i < len (nums)-1 :
           
            if nums[i+1] == nums[i]+1:
                count = count+1
                #result = max (result,count)
     
            elif nums[i+1] == nums[i]: 
                count =count 
                #result = max (result,count)
            else :
                 #result = max (result,count) 
                 count = 1
            result = max (result,count) 
            i = i+1

        return result 

        