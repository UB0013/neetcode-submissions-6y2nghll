from typing_extensions import DefaultDict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m  = DefaultDict(list)

        for s in strs : 
            key = tuple (  sorted (s) ) 
            m[key].append(s) 

        return list(m.values())
        