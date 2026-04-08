class TimeMap:

    def __init__(self):
        self.mapp = defaultdict(list)

        

    def set(self, key: str, value: str, timestamp: int) -> None:
       

        self.mapp[key].append([timestamp,value])
        #print(self.mapp)

    def get(self, key: str, timestamp: int) -> str:
        values = self.mapp.get(key,[])
        #print (values)
        res = ""


        l = 0
        r = len(values)-1
        while l<=r : 
            mid = (l+r)//2
            if values[mid][0] <= timestamp :
                res = values[mid][1]
                l = mid +1
            else :
                r = mid -1
        return res 
            
            


        
