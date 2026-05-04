class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0 

        for i in range (len(s)):
            l = i 
            r = i 
            while l >= 0 and r < len(s) and s[r] == s[l] :
                count = count + 1 
            
                l -= 1 
                r += 1

            l = i 
            r = i +1 

            while l >= 0 and r < len(s) and s[r] == s[l] :
                count = count + 1 
            
                l -= 1 
                r += 1
        return count 

        