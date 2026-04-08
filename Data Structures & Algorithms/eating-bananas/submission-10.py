class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        result = r

        
        while l <=r : 
            rate = (l+r)//2
            time =0
            for p in piles:
                time = time + math.ceil((p/rate))
                
            if time > h: 
                l = rate+1
            else : 
                r = rate-1
                result = min (result,rate)

        return result

        



            


    