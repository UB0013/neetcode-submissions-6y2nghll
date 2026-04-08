class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0 
        l = 0 
        r = 0 
        rep = set()

        while r < len(s): 
            if s[r] in rep :
                rep.remove(s[l])
                l += 1
            else : 
                rep.add(s[r])
                res = max(res, r-l+1)
                r = r+1 
        return res 
        



        