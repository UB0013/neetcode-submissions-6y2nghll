class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set (nums)
        print(unique)
        res =1 
        if len(nums) == 0 :
            return 0 
        count = 1 
      
        for n in unique :
            while n+1 in unique :
                count  = count +1
                n = n+1
                res = max(res,count)
            else :
                count = 1
            
        return res 




        