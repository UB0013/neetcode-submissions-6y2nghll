class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacencymap  =  defaultdict(list)
        visit = set()
        for c1,c2 in prerequisites : 
            adjacencymap[c1].append(c2)
        #print (adjacencymap)

        def dfs (course) :
            if adjacencymap[course] == [] : 
                return True 
            if course in visit : 
                return False 
            
            visit.add(course)
            for crs in  adjacencymap[course] :
                if not dfs(crs):
                    return False 
            visit.remove(course)
            adjacencymap[course] = []
            
            return True 



            



        for i in range(numCourses) : 
            if dfs (i) == False : 
                return False  
        return True 






        