class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights) - 1
        area = 0 
        result = 0 

        while l < r : 
            area = (min(heights[l],heights[r])) * (r-l)
            result = max (result,area)
            if heights[l] < heights[r] : 
                l = l +1 
            elif heights[r] <  heights[l]  : 
                r=r-1
            else : 
                l = l +1
        return result 
            




        