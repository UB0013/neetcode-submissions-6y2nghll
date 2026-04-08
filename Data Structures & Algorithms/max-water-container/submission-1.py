class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights)-1
        res = 0 
        while l < r : 
            length  = min (heights[l], heights[r])
            b = r-l 
            area = length * b 
            print (area)
            res = max (res,area)
            if heights[l] <= heights[r] :
                l  = l+1 
            elif heights[l] > heights[r]:
                r = r-1 
        return res 
        


        