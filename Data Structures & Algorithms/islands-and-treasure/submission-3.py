from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        q = deque ()
        directions = [(1,0), (-1,0),(0,1), (0,-1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))

        while q :
            r , c = q.popleft()
            for mr , mc in directions :
                nr = r + mr 
                nc = c+ mc
                if nr <0 or nc < 0 or nr >= rows or nc >=  cols or grid[nr][nc] != 2147483647:
                    continue 
                grid[nr][nc] = 1+ grid[r][c]
                q.append((nr,nc))
        


