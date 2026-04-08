class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set (nums)
        print(unique)
        res =1 
        if len(nums) == 0 :
            return 0 
        count = 1 
      
        for n in unique :
            if n-1 not in unique : 
                count =1 
                while n+1 in unique :
                    count =count +1
                    n=n+1
                res = max(res,count)
        return res 




        