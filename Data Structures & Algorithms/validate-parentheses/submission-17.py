class Solution:
    def isValid(self, s: str) -> bool:
        mapp = {"}" : "{" , "]" : "[" , ")" : "("}
        stack =[]
        for c in s :
            if  stack :
                if c in mapp.values() : 
                    stack.append(c)
                elif stack[-1] != mapp[c] :
                    return False
                else :
                    stack.pop()
            else :
                if c in mapp.values():
                    stack.append(c)
                else :
                    return False
        if stack :
            return False
        else :
            return True 