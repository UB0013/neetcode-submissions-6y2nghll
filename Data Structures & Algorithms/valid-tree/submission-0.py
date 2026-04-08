class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if not n : 
            return True 

        adjmap = {i: [] for i in range (n)}

        for n1 , n2 in edges : 
            adjmap[n1].append(n2)
            adjmap[n2].append(n1)
        

        visit = set ()
        

        def dfs (node,prev):
            if node in visit :
                return False
            visit.add(node)

            for i in adjmap[node] :
                if i == prev :
                    continue 
                if dfs (i,node) == False:
                    return False
            
            return True 

        return dfs(0, -1) and len(visit) == n

                 
        
        
        print(adjmap)
        return False 
        