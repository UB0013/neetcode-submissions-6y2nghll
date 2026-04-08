# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0 

        def dfs (node,maxval) : 
            nonlocal count 
            if not node :
                return 0
            if node.val >= maxval:
                count = count + 1 
            maxval = max(node.val,maxval)
            dfs (node.left,maxval )
            dfs(node.right,maxval)

            return count 

        return dfs (root, root.val)


       