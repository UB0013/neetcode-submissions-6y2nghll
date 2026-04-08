class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0 
        r = len(height)-1
        maxL, maxR =  height[l],height[r]  
        sum = 0 

        while l < r:
            if maxL < maxR : 
                l = l+1
                maxL = max(maxL, height[l])
                sum = sum + maxL-height[l]
            else: 
                r = r-1
                maxR = max(maxR,height[r])
                sum = sum + maxR-height[r]
        return sum 









            