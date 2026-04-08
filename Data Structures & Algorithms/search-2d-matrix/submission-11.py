class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0 
        bottom = len(matrix)-1
        while top <= bottom : 
            row = (top + bottom) //2

            if target < matrix[row][0]:
                bottom = row-1
            elif target >=  matrix[row][0] :
                if target <= matrix[row][-1]: 
                    break 
                top = row + 1 
           
        if not top <=bottom :
            return False


        print (row)

        
        l = 0 
        r = len(matrix[0])
        print(r)

        while l <= r :
            mid = (l + r)// 2
            if target > matrix[row][mid]: 
                l = mid +1
            elif target < matrix[row][mid]:
                r = mid-1
            else :
                return True  
            
        return False 


        


        