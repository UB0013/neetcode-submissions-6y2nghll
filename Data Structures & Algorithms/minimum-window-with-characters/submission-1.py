class Solution:
    def minWindow(self, s: str, t: str) -> str:
        havemap  = {}
        needmap = {}
        minlen = float("infinity")
        result = [-1,-1]
    

        for c in t : 
            needmap[c] = 1+ needmap.get(c,0)

        have = 0 
        need = len (needmap)
        l = 0 
        
        for r in range(len(s)) : 
            havemap [s[r]] = 1 + havemap.get(s[r],0)
            if s[r] in needmap and needmap[s[r]] == havemap[s[r]] : 
                have += 1
            while need == have : 
                
                if r-l+1 < minlen : 
                    result = s[l:r+1]
                    minlen = r-l+1 
                havemap [s[l]] -=1 
              
                if s[l] in needmap and havemap[s[l]] < needmap[s[l]] :
                    have -=1 
                l=l+1
        return "" if minlen == float("infinity") else result


                


        

        