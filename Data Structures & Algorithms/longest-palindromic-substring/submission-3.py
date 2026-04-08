class Solution:
    def longestPalindrome(self, s: str) -> str:

        reslen = 0 
        res = s[0]
        lens = len(s)

        for i in range (lens):
            l = i 
            r = i 
            while l >= 0 and r < lens  and s[l] == s[r] :
                if r-l+1 > reslen :
                    res = s[l:r+1]
                    reslen = r-l+1
                l -= 1 
                r += 1
            l= i 
            r = i+1

            while l >= 0 and r < lens  and s[l] == s[r] :
                if r-l+1 > reslen :
                    res = s[l:r+1]
                    reslen = r-l+1
                l -= 1 
                r += 1

        return res 

                


        