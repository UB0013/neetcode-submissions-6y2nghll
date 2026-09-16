class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = max(piles)
        l = 1
        r = n 
        k = n 
        
        while l<=r : 
            mid = (l+r)//2
            print(mid)
            hours = 0 
            for i in piles : 
                print(i//mid)
                hours += math.ceil(i/mid)
            print(hours)
            if hours > h :
                l = mid +1 
            else :
                r = mid-1
                k = min (k,mid)
        return k 
            



