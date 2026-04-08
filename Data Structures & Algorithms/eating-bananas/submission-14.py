import math 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
         

        k =max(piles)
        
        res = k 
        r = max(piles)
        l = 1
        while l <= r : 
            k = (l+r) //2
            total=0
            for n in piles : 
                total = total + math.ceil(n/k)
            if total > h : 
                l = k+1
            elif total <= h:
                res = k 
                r = k -1 
        return res  








        
        