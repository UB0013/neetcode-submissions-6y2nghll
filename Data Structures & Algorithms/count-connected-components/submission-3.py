class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range (n)]
        rank = [1]*n
        count = n 
        def union (n1,n2):
            p1 = find (n1)
            p2 = find (n2)
            if p1 == p2 : 
                return False
            if p1 != p2 :
                if rank[p1] >= rank [p2] :
                    parent[p2] = p1
                    rank [p1] = rank[p1] + rank [p2]
                elif rank[p1] < rank [p2]:
                    parent [p1] = p2
                    rank[p2] = rank[p1] + rank [p2]
            return True 


        def find (n):
            if parent [n] != n :
                parent[n] = find(parent[n]) #find(2)
            return parent[n]

  
        for n1 ,n2 in edges : 
            if union(n1,n2):
                count -= 1  
        print ()
        return count 

       





        