class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        mapp = {i:[] for i in range(n)}
        for n1,n2 in edges:
            mapp[n1].append(n2)
            mapp[n2].append(n1)
        visit = set ()
        componentes = 0
        
        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for edges in mapp[node]:
                dfs(edges)

        

        for i in range(n):
            if i in visit:
                continue 
            else: 
                dfs(i)
                componentes +=1 
        return componentes 

        