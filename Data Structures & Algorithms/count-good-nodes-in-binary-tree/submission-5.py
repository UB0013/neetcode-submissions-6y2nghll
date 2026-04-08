# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node,maxval): 
            if not node:
                return 0
            if node.val >= maxval :
               result =1
            else : 
                result = 0
            maxval = max(maxval,node.val)
            result += dfs (node.left,maxval)
            result += dfs(node.right, maxval)
            return result

        return dfs (root,root.val)



       