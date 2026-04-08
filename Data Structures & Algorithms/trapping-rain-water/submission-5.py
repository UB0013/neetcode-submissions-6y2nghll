class Solution:
    def trap(self, height: List[int]) -> int:
        lmax = height[0]    # 0 
        rmax = height[len(height)-1] # 1 
        l = 0 
        r = len(height)-1
        water = 0
        while l < r : 
            #water += max (min(lmax,rmax) - heights[i], 0) 
            if height[l] <= height [r] : 
                water += max (min(lmax,rmax) - height[l], 0) 
                l = l +1 
                lmax = max(lmax, height[l]) # 3
            else : 
                water += max (min(lmax,rmax) - height[r], 0)
                r = r - 1 
                rmax = max(rmax, height[r]) # 3
        return water

            
           
          