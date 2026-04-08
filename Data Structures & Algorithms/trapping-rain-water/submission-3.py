class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0 
        r = len(height)-1 
        res = 0 

        lmax = height [0]
        rmax = height [r]
        sum = 0 

        while l < r : 
            if lmax < rmax : 
                l = l+1 
                lmax = max(lmax, height[l])
                sum += lmax - height [l]
            else :
                r =  r-1
                rmax = max(rmax,height[r])
                sum = sum +  rmax - height[r]
        return sum
        


        

       