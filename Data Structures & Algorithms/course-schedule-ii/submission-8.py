class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = {i : [] for i in range(numCourses) }
        output =[]
        done = set()
        for element in prerequisites:
            crs = element[0]
            pre = element [1]
            premap[crs].append(pre)
        visit = set ()
        def dfs (crs):
            if crs in visit : 
                return False 
            #if premap[crs] == []:   # already processed
                #return True

            if crs in done:
                return True
            

            visit.add(crs)
            for pre in premap[crs]: 
                if dfs (pre) == False : 
                    return False
            visit.remove (crs)
            #premap[crs] = []

            done.add(crs)
            
            output.append(crs)

            return True 
        for crs in range (numCourses):
            if dfs (crs) == False:
                return [] 
        return output 