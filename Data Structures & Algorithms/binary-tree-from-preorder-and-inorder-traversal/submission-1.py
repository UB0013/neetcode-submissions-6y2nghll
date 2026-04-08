# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # build the hashmap once
        idx_map = {val: i for i, val in enumerate(inorder)}
        rootpointer = 0

        def dfs(l, r):
            nonlocal rootpointer
            if l >r :
                return None
            rootval = preorder[rootpointer]
            rootpointer += 1 
            root = TreeNode(rootval)
            mid = idx_map[rootval]
            root.left = dfs(l,mid-1)
            root.right = dfs(mid+1, r)
            return root 

        return dfs(0, len(inorder)-1)
