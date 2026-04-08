"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node : 
            return None 
        copymap = {}

        def dfs (node):
            if node in copymap : 
                return copymap[node]
            copy = Node(node.val)
            copymap[node] = copy 
            for neighb in node.neighbors : 
                copy.neighbors.append(dfs(neighb))
            return copy 
        return dfs(node)


        