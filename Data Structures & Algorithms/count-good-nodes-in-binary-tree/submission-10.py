# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
       
        count = 0 
    
        def dfs (root,maxx) :
            nonlocal count 
            if not root :
                return 0
            #maxx = max (maxx,root.val) 
            if root.val >= maxx :
                maxx = root.val #4
                count = count+1
            dfs(root.left,maxx)
            dfs (root.right,maxx)
        
        dfs (root,float("-inf"))
        return count





        