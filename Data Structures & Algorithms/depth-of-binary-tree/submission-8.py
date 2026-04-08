# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root :
            return 0 
        count = 1
        def dfs(root) : 
            if not root : 
                count = 0
                return count  
            return max (1 + dfs(root.left), 1 + dfs(root.right))
        return dfs(root)
        