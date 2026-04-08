# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        index = {val:i for i , val in enumerate (inorder)}
        rootpointer = 0

        def dfs (l,r):
            nonlocal rootpointer
            if l > r :
                return None 
            nodeval = preorder[rootpointer]
            rootpointer +=1 
            mid = index[nodeval]
            node = TreeNode(nodeval)
            node.left = dfs (l,mid-1)
            node.right = dfs (mid+1, r)
            return node 
        return dfs (0, len(inorder)-1)