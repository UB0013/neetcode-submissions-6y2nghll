from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res  = [[]]
        mapp = defaultdict(list)
        
        for s in strs : 
            key = tuple(sorted (s)) 
            if key not in mapp : 
                mapp[key] = []
            mapp[key].append(s) 
        res = list(mapp.values())

        return res 
        