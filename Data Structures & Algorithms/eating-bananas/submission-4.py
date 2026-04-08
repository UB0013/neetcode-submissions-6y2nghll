class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 
        r = max(piles)
        res = r
        
        while(l<=r):
            mid = (l +r)//2
            sum = 0
            for each in piles : 
                sum = sum + math.ceil(each/mid) 
            if sum > h : 
                l = mid +1 
            elif sum <= h : 
                r = mid - 1 
                res = min(res,mid)
        return res 
            

            
        