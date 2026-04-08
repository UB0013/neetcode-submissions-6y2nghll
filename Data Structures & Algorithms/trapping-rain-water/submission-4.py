class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)-1 
        lmaxarr = [0]*(n+1) 
        rmaxarr = [0]*(n+1)
        lmax =0 
        rmax =0 
        result = 0
        
        
        l = 0 
        r = n 
        for i,h in enumerate (height):
            lmax  = max (lmax,height[i])
            lmaxarr[i] = lmax
        for i in range(n , -1 , -1 ):
            rmax = max (rmax,height[i])
            rmaxarr[i] = rmax
        for i in range(n): 
            result = result + (min (lmaxarr[i],rmaxarr[i]))- height [i]
        
        return result
        





        

       