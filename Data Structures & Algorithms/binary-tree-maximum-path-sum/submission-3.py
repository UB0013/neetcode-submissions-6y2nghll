# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        result = root.val

        def dfs(root):
            nonlocal result 
            if not root : 
                return 0
            l = dfs (root.left)
            r = dfs(root.right)
            ## SIMPLE CHECK TO AVOID NEGATIVES

            l = max(0,l)
            r = max(0,r)

            result = max(result, root.val + l + r)
            return root.val + max(l,r)
        dfs(root)
        return result 

       