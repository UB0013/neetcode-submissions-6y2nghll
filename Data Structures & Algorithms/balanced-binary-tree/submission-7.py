class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs (curr): 
            if not curr : 
                return [True,0]
            
            left = dfs(curr.left)
            right = dfs (curr.right)
            depth = 1 + max (left [1],right[1])
            if  left[0] and right[0] and abs(left[1] - right[1]) <= 1 :  
                return [True, depth]
            else :
                return [False, depth] 

        if not root:
            return True
        else: 
            result =  dfs(root)[0]
            return result
      
        
        
            
            
        
       