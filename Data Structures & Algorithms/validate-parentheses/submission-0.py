class Solution:
    def isValid(self, s: str) -> bool:
        opentoclose = {"(":")", "{" : "}" , "[" : "]"}
        stack =[]

        for c in s: 
            if c in opentoclose:
                stack.append(c)
            elif stack and opentoclose[stack[-1]]== c:
                stack.pop()
            else : 
                return False
        

        return not stack 




        
        
        