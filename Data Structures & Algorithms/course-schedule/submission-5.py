class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i: [] for i in range(numCourses)}
        for element  in prerequisites:
            crs = element[0]
            pre = element[1]
            premap[crs].append(pre)
        visit = set()
        def dfs (crs) : 
            if premap[crs] == []:
                return True 
            if crs in visit : 
                return False 
            visit.add(crs)
            for pre in premap[crs]: 
                dfs (pre)
                if dfs (pre) ==False :
                    return False 
            visit.remove(crs)
            premap[crs] =[]
            return True

        for crs in range (numCourses): 
            if dfs (crs) == False:
                return False 

        return True


            
            
            

        