class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack =[]
        area  = 0 

        for i , h in enumerate (heights) : 
            start = i 
            while stack and stack [-1][1] > h :
                index, hh = stack.pop()
                area = max(area, hh * (i-index)) 
                start = index
            stack.append([start,h])
        while stack : 
            index, hh = stack.pop()
            area = max(area, hh * ((len(heights)-index)))

        return area 
                   




            

 