class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0]* len(temperatures)
        tempstack = []

        for i, t in enumerate (temperatures) : 
            
            while tempstack and tempstack[-1][0] < t : 
                temp, index = tempstack.pop()
                res [index] = i-index
            if len (tempstack) == 0 :
                tempstack.append([t,i])
                continue
            if tempstack and tempstack[-1][0] >= t : 
            #else : 
                tempstack.append([t,i])
            
        return res 

            
            

            
        

            


        