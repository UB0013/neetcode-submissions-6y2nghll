class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len (grid)
        cols = len(grid[0])
        q = deque()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        for r in range(rows):
            for c in range (cols):
                if grid[r][c] ==0 :
                    q.append((r,c))
        
        while q : 
            for i in range (len(q)):
                r, c = q.popleft()
                for mr , mc in directions : 
                    nr = r + mr
                    nc = c + mc 
                    if nr >=0 and nc >= 0 and nr < rows and nc < cols and grid[nr][nc] == 2147483647 : 
                        grid[nr][nc] = 1 + grid[r][c]
                        q.append((nr,nc))
        





        