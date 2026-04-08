class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = { i :  [] for i in range(numCourses )}

        for element in prerequisites: 
            crs = element[0]
            pre = element[1]
            premap[crs].append(pre)

        visit = set ()

        def dfs (crs):
            if crs in visit :
                return False
            
            if not premap[crs] :
                return True 

            visit.add(crs)
            for pre in premap[crs]: 
                if dfs (pre) == False :
                    return False
            visit.remove(crs)
            premap[crs] = []
            return True 

        for c in range(numCourses):
            if dfs (c) == False :
                return False
        return True 


            
            




        print (premap ) 
        return False


        