class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        r = 0 
        result = 0 
        maxlen = 0 
        dupes = set ()
        while r < len(s): 
            
            if s[r] not in dupes: 
                #dupes.add(s[r])
                maxlen = r-l+1
            while s[r] in dupes :
                dupes.remove(s[l])
                l = l +1 
            dupes.add(s[r])
            maxlen = r-l+1
            print (maxlen)
            result = max(result, maxlen)
            r = r+1 
        return result

     

         
        

        