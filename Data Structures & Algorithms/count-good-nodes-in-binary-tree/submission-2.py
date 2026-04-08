# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs (root , maxval): 

            result = 0 
            if not root :
                return 0
            if root.val >= maxval : 
                result = result +1 
            if root.val <= maxval :
                result = result +0
            maxval = max(maxval,root.val)
            result = result +  dfs(root.left, maxval) + dfs(root.right,maxval)
            return result
             

        return dfs(root,root.val)

        