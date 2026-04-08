# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = 0 

        def dfs (root):
            nonlocal res 
            print (1)

            if p.val  < root.val and q.val < root.val :
                dfs(root.left)
            elif p.val  > root.val and q.val> root.val:
                dfs (root.right)
            else: 
                res = root 
                return   
        dfs (root)
        return res

        