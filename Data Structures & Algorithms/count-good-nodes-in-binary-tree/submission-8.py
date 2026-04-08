# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        check = root.val
        count = 0
        def dfs (root,check) :
            nonlocal count
            if not root :
                return 0
            if root.val >= check :
                count = count +1 
            check = max(check,root.val)
            dfs(root.left,check)
            dfs(root.right,check)
            return 0
        dfs (root,root.val)
        return count 
        
        