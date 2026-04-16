class Solution:
    def isValid(self, s: str) -> bool:
        mapp = {"}" : "{" , "]" : "[" , ")" : "("}
        stack =[]
        for c in s :
            if c not in mapp : 
                stack.append(c)
            else: 
                if not stack or stack[-1] != mapp[c] :
                    return False
                stack.pop()
         
                    
        if stack :
            return False
        else :
            return True 