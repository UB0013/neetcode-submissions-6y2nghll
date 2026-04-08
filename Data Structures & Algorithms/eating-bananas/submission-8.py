class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        
        returnrate = r

        while l <=r : 
            mid = (l+r)//2
            result = 0 
            for p in piles :
                rate = math.ceil(p/mid) 
                result = result + rate  
            if result > h : 
                l = mid + 1 
            elif result<=h : 
                r = mid-1 
                returnrate = min (returnrate, mid)
             
                

        return returnrate

            
        