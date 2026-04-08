class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)
        
        res = 0

        #print(math.ceil(3/2))

        
        while l <=r : 
            time = 0

            rate = (l+r)//2
            for i, n in enumerate (piles):
                time = time + math.ceil(n/rate)
            print(time)
            if time > h : 
                l = rate +1 
            else : 
                r = rate -1 
                res = rate
        return res

            

            



        return r 

        # 

        