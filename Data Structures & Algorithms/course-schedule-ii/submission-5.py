class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = {i : [] for i in range(numCourses) }
        output =[]

        for element in prerequisites:
            crs = element[0]
            pre = element [1]
            premap[crs].append(pre)
        
        visit = set ()

        def dfs (crs):
            if crs in visit : 
                return False 
            visit.add(crs)
            for pre in premap[crs]: 
                if dfs (pre) == False : 
                    return False
            visit.remove (crs)
            premap[crs] =[] 
            if crs not in output :
                output.append(crs)
            return True 
        
            
            
            


        for crs in range (numCourses):
            if dfs (crs) == False:
                return [] 
        return output 