class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        row = set()
        col = set()
        posdiag = set()
        negdiag = set()
        res =[]
        def backtrack (r):
            if r == n : 
                copy = ["".join(x) for x in board]
                res.append(copy)
                return 
            for c in range (n):
                if c  in col or c+r  in posdiag or c-r  in negdiag :
                    continue
                col.add(c)
                posdiag.add(c+r)
                negdiag.add(c-r)
                board[r][c] = "Q"

                backtrack (r+1)

                col.remove(c)
                posdiag.remove (c+r)
                negdiag.remove(c-r)
                board[r][c] = "."
        backtrack (0)
        return res 


