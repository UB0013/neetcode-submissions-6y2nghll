class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if not n :
            return True 
        adjmap = { i : [] for i in range(n)}

        for n1 , n2 in edges : 
            adjmap[n1].append(n2)
            adjmap[n2].append(n1)
        visit = set()
        
        def dfs (curr , prev) : 
           
            if curr in visit : 
                return False 
            visit.add(curr)
            
            for neigh in adjmap[curr]:
                if neigh == prev : 
                    continue 
                if dfs (neigh,curr) == False:
                    return False 
            return True 

        return dfs(0,-1) and len (visit) == n 
            


        