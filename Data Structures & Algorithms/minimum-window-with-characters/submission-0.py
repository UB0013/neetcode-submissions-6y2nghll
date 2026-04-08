class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countt , window = {},{}

        for c in t :
            countt[c] = 1+ countt.get(c, 0)
        have , need = 0, len(countt)
        reslen = float("infinity")
        res = [-1,1]
        r, l = 0,0

        for r in range(len(s)):
            c =s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countt and window[c] == countt[c]:
                have  +=1
            
            while have == need:
                if (r-l+1) < reslen:
                    res = s[l:r+1]
                    reslen = r -l +1
                
                window[s[l]] -= 1
                if s[l] in countt and window[s[l]] < countt[s[l]]:
                    have -= 1
                l = l+1

        #l, r = res
        return res if reslen != float("infinity") else ""

        
                




        