class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = [i for i in range(n)]
        rank = [1]* (n)

        def find (n1) : 
            if parent[n1] == n1 : 
                return n1 
            return find (parent[n1])


        def union (n1, n2 ) : 
            nonlocal n
            p1 = find (n1)
            p2 = find (n2)

            if p1 != p2 : 
                if rank[p1] < rank [p2] :
                    p1,p2 = p2,p1 
                parent[p2] = p1
                rank[p1] = rank [p1] +rank[p2] #try 1 
                n -=1 
            else:
                return False 

            
        for n1,n2 in edges : 
            if union (n1,n2)  == False:
                return False
        if n == 1 :
            return True 
        return False
    
    
    

        


