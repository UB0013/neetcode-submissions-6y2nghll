class Solution:
    def isValid(self, s: str) -> bool:

        if not s :
            return True

        maps = {')':'(', ']':'[','}':'{'}
        stack= []

        #print (maps['}']) 

        for c in s : 
            if c not in maps : 
                stack.append(c)
            elif stack and stack [-1] == maps[c] :
                stack.pop()
            else : 
                return False
            

        if not stack : 
            return  True
        return False
        