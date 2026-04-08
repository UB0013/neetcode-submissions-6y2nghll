class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count  = {}
        r= 0 
        l = 0 

        for c in s:
            count[c] = 1 + count.get(c,0)
            while (r-l+1) - max (count.values()) > k :
                count [s[l]] -= 1
                l = l+1
            
            res =max(res,r-l+1)
            r = r+1



        

        return res

       