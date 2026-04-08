class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        
        for string in strs : 
            s += str (len (string))  + "#" +  string
        print (s)
        return s 


    def decode(self, s: str) -> List[str]:
        ans = [ ]
        i=0

        while i < len (s): 
            j = i
            while s[j] != '#':
                j += 1 
                length = int (s[i:j])
            i = j+1
            j = i + length 
            ans.append(s[i:j])
            i = j 
        return ans


            



