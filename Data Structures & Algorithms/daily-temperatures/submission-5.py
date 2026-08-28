class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0]*(len(temperatures))
        stack = []

        for i, t in  enumerate(temperatures) : 
            while stack and stack[-1][1]< t :
                indexT, stackT= stack.pop()
                result[indexT] = i-indexT
            stack.append([i,t])
        return result 



