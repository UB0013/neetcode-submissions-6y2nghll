class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        x = set(nums)
        res = 0
        count =0


        for n in nums : 
            if n-1 not in x : 
                count = 1 
                while n + count in x : 
                    count = count +1 
            res = max(count,res)

        return res
            
            