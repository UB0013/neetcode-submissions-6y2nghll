class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l =0 
        r = 0 
        count = {}
        res = 0 
        for c in s : 
            count[c] = 1+ count.get(c,0)
            if (r-l+1) - max(count.values()) > k :
                count[s[l]] -= 1
                l = l+1
            res = max(res, r-l+1)
            r = r +1 
        return res 

        
        