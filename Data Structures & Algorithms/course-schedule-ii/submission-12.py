class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacencymap  =  defaultdict(list)
        visit = set()
        result = [] 
        for c1,c2 in prerequisites : 
            adjacencymap[c1].append(c2)
        #print (adjacencymap)

        def dfs (course) :
            nonlocal result 
            if course in visit : 
                return False 
            if adjacencymap[course] == [] : 
                if course not in result : 
                    result.append(course)
                return True 
            
            visit.add(course)
            for crs in  adjacencymap[course] :
                if  dfs (crs) == False :
                    return False 
            visit.remove(course)
            adjacencymap[course] = []
            result.append(course)
            return True 

        for i in range(numCourses) : 
            if dfs (i) == False : 
                return []
        return result 






        