class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        r = 0
        res = set ()
        reslen = 0 

        while r < len(s):
            while s[r] in res and l < len(s):
                res.remove(s[l])
                l = l+1
            res.add(s[r])
            reslen = max  (reslen, len(res))
            r = r +1 
        return reslen 


         
        

        