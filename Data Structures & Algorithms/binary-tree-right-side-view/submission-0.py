# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

   


        q = collections.deque()
        result =[]
        q.append(root)

        while q : 
            #level = []
            rightside = None 
            
            qlen = len(q)
            for i in range (qlen): 
                node = q.popleft()
                if node :
                    #level.append(node.val)
                    rightside =node
                    q.append(node.left)
                    q.append(node.right)

            if rightside :
                result.append(rightside.val)

        return result 
        