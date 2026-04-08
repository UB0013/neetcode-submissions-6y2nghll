class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxA     = 0 
        breadth = 1 
        stack =[]
        for i, h in enumerate (heights):
            start = i 
            while stack and stack[-1][1]>h :
                area = 0 
                stackI,stackH = stack.pop()
                start = stackI
                area = stackH * (i-stackI)
                maxA = max(maxA,area)
            stack.append([start,h]) 

        for i,h in stack : 
            maxA = max(maxA, h*(len(heights)-i))

        return maxA





      






        