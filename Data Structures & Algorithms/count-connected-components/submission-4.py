class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        par = [i for i in range (n)]
        rank = [1]*n


        def find(n1):
            if par[n1] == n1 : 
                return n1
            par[n1]= find (par[n1])
            return par[n1]

        def union (n1,n2) : 
            nonlocal n 
            p1 = find(n1)
            p2 = find(n2)
            if p1 != p2 :
                if rank[p1] < rank[p2]:
                    p1,p2 = p2,p1
                par[p2] = p1
                rank [p1] = rank[p2] + rank[p1]
                n -= 1 
        
        for n1,n2 in edges  :
            union (n1,n2)


        return n
        
        

        