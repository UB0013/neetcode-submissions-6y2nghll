class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs :
            res += str(len (s))  + "#" + s
        print(res)
        return res


    def decode(self, s: str) -> List[str]:
        i = 0 
        res = []
        while i < len(s): 
            j = i 
            while s[j] != "#":
                j=j+1
            l = int(s[i:j])
            res.append(s[j+1:j+l+1])
            i= j+l+1
        return res


            
        return res





