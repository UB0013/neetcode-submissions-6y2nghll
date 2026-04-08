# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # def dfs (root, left, right):
        #     if not root:
        #         return True
        #     if root.val >  left and root.val<  right:
        #         return ( dfs (root.left, left, root.val) and dfs (root.right, root.val, right)) 
        #     else:
        #         return False
        # return dfs(root, float("-inf"),float("inf"))

# AS WE GO LEFT THE UPPER BOUNDRY SHRINKS TO NODE VAL
# AS WE GO RIGHT THE LOWER BOUNDRY SHRINKS 

    
            

        def dfs (node,ub , lb):
            if not node :
                return True

            if node.val < ub and node.val > lb :
                
                
                return  dfs (node.left, node.val, lb) and dfs (node.right, ub, node.val)
            else :
                return False
        return dfs (root, float("inf"), float("-inf"))


            


    