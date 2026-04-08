# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root) : 
            if not root :
                depth = 0 
                return [True, depth ]
            left = dfs(root.left)
            right = dfs(root.right)
            if left[0] and right [0] and abs(left [1] - right[1]) <= 1:
                balance = True
            else:
                balance = False
            # returning at this node 
            depth = max(1+ left [ 1 ], 1+ right [ 1])

            return [balance,depth]

        res = dfs (root)
        return res[0]


            