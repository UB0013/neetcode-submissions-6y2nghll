class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0   # empty tree has depth 0

            left = dfs(node.left)
            if left == -1:    # left subtree unbalanced
                return -1

            right = dfs(node.right)
            if right == -1:   # right subtree unbalanced
                return -1

            if abs(left - right) > 1:   # current node unbalanced
                return -1

            return 1 + max(left, right) # depth if balanced

        return dfs(root) != -1
