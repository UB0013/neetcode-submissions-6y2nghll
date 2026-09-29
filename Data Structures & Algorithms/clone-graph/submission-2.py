"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        #       { ORG1 (val , neighbors(ORG2, ORG3)) : copy1 (val,copy2,copy3 )
        #        ORG2 (v, n o1 o2 ) :   copy2 )}

        copymap = {None:None}

        #node.val 
        #node.neighbors

        def dfs (node): 
           
            if node in copymap: 
                return copymap[node]
            copy = Node (node.val)
            copymap[node] = copy 
            for n in node.neighbors :
                copyn = dfs(n)
                copy.neighbors.append(copyn)
            return copy 
        dfs ( node )
        return copymap[node]
