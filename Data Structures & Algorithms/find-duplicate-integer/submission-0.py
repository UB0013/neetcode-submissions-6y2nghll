class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash = set ()
        for n in nums : 
            if n in hash : 
                res = n 
            else : 
                hash.add(n)
        return res


        