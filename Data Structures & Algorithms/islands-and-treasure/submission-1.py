from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        for r in range (rows) :
            for c in range (cols) : 
                if grid[r] [c] == 0:
                    q.append((r,c))
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while q :
            row , col  = q.popleft()

            for mr, mc in directions :  
                nr , nc = row +mr , col + mc
                if (nr < 0 or nr >= rows or nc <0 or nc >= cols  or grid[nr][nc]!=2147483647):
                    continue 
                grid[nr][nc] = grid[row][col] +1
                q.append((nr,nc))
                
        

