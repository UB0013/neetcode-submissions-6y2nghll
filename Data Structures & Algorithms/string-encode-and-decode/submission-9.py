class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs :
            count = 0
            for i in s :
                count+=1
            result += str(count)+'#'+s
        print(result)
        return result


    def decode(self, s: str) -> List[str]:
        result = [] 
        i= 0 
        count = 0 
        while i < len(s):

            j = i+1
            # count = count +1 
            # if count == 4:
            #     break 
            while j < len(s): 
                if s[j] == "#":
                    strlen = int(s[i:j])
                    result.append(s[j+1:j+1+strlen])
                    i = j +1 + strlen 
                    break 
                j = j +1
            
        return result
