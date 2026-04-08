class Solution:



    def letterCombinations(self, digits: str) -> List[str]:
        res =[]
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        if not digits :
            return []
        def backtrack (i,curr):
            if i == len(digits):
                res.append("".join(curr))
                return 
            for c in digitToChar[digits[i]]:
                curr.append(c)
                backtrack (i+1, curr)
                curr.pop()
               
        backtrack (0, [])
        return res 
        
            

                
            
          
        