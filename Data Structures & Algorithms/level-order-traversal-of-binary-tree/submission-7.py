# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root) 
        result = [] 
        while q : 
            lenq = len(q)
            dummy =  []
            for i in range (len(q)) : 
                node = q.popleft()
                
                if node : 
                    q.append(node.left)
                    q.append(node.right)
                    dummy.append(node.val)
            if dummy :  
                result.append(dummy)
        return result 



        #result = [[1], [2,3], [4,5,6,7], ]




        