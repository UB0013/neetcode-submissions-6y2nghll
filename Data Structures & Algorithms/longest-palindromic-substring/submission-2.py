class Solution:
    def longestPalindrome(self, s: str) -> str:
        reslen = 0 

        for i in range (len(s)):
            l = i 
            r = i 
            while l >= 0 and r <len(s) and s[l] == s[r]:
                if (r-l +1) > reslen: 
                    result  = s [l:r+1]
                    reslen = len(result )
                l = l-1
                r =r+1

            l = i 
            r = i +1 
            while l >= 0 and r <len(s) and s[l] == s[r]:
                if (r-l+1) > reslen: 
                    result  = s [l:r+1]
                    reslen = len(result )
                l = l -1
                r =r+1

        return result 
        


        
        