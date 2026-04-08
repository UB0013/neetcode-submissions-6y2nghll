class Solution:
    def isValid(self, s: str) -> bool:
        opentoclose = {"(":")", "{" : "}" , "[" : "]"}
        stack =[]

        for c in s :
            if c in opentoclose :
                stack.append(c)
            elif stack and c == opentoclose[stack[-1]]:
                stack.pop()
            else: 
                return False 

        return not stack

        
        
        