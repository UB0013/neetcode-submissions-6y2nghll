class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        mapp = {i : [] for i in range(n)}

        for n1, n2 in edges:
            mapp[n1].append(n2)
            mapp[n2].append(n1)
        print(mapp)
        visit = set ()

        def dfs (node,prev):
            
            if node in visit:
                return False 
            visit.add(node)
            for edges in mapp[node]:
                if edges == prev:
                    continue
                if dfs (edges, node) == False:
                    return False 
            return True 

        return dfs(0,-1) and len(visit) ==n 

