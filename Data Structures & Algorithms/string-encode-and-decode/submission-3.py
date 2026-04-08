class Solution:

    def encode(self, strs: List[str]) -> str:
        c =""
        for s in strs:
            l = len(s)
            #print("".join((str(l)+"#"+s)))
            c +="".join((str(l)+"#"+s))
        print (c)
        return c


    def decode(self, s: str) -> List[str]:
        res =[]
        i =0
        while i < len(s):
            j= i 
            while s[j] != "#":
                j =j+1
            
            l = int(s[i:j])
            val = s[j+1:j+1+l]
            res.append(val)
            i = j+1 +l
            j = i
        return res
