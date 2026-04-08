class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = set ()
        for n in nums:
            if n not in dups:
                dups.add(n)
            else : 
                return True 
            print (dups)
        
        return False 
        