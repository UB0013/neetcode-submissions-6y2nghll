class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mapp = {}
        mapp2 = { }
        for c in s1 :
            mapp[c] = 1 + mapp.get(c,0)
        #print (mapp)

        l =0 
        r =0 
        while r in range(len(s2)):
            mapp2[s2[r]] = 1+mapp2.get(s2[r],0)

            if r-l+1 > len(s1):
                mapp2[s2[l]] -= 1
                if mapp2[s2[l]] == 0 :
                    del mapp2[s2[l]]
                l=l+1
            if mapp ==mapp2:
                return True 
            r = r+1
            
        return False






        