class Solution:
    def isValid(self, s: str) -> bool:
        opentoclose  = {")": "(", "]":"[" , "}":"{"}
        stack = []
        for c in s :
            if c not in opentoclose: 
                stack.append(c)
            else :
                if stack and  stack [-1] == opentoclose[c]:
                    stack.pop()
                else:
                    return False

        if not stack :
            return True 
        else:
            return False
                

        

            


        