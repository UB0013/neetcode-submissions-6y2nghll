class Solution:
    def trap(self, height: List[int]) -> int:

        lmax = height[0]
        rmax =  height[-1]
        l, r = 0, len(height)-1
        water = 0 

        while  l< r: 
            if height[l] <= height[r] :
                water += max( min (lmax,rmax) - height[l], 0) 
                l = l+1 
                lmax = max( height[l], lmax)

            elif  height[l] > height[r]: 
                water += max( min (lmax,rmax) - height[r], 0) 
                r = r -1 
                rmax = max( height[r], rmax)
        return water 

            




        