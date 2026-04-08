class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowzero = False
        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(rows):
            for c in range( cols) :
                if matrix[r][c] == 0 :
                    matrix[0][c] = 0 
                if  matrix[r][c] == 0 and r > 0 :
                    matrix[r][0] = 0
                if r == 0 and  matrix[r][c] == 0 :
                    rowzero = True
        
        for r in range(1,rows):
            for c in range (1,cols):
                if matrix [0][c] == 0 :
                    matrix[r][c] = 0 
                if matrix[r][0] == 0: 
                    matrix[r][c] = 0 

        
       

        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        if rowzero :
            for c in range(cols) :
                matrix[0][c] = 0 

  

       



        
        