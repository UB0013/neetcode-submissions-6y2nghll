class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len (grid[0])
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        islands =0 


        def bfs (r,c):
            q = collections.deque ()
            q.append ((r,c))
            while q :
                r , c = q.popleft()
                for mr , mc in directions :
                    nr, nc = mr +r , mc +c

                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols  or grid[nr][nc] == "0" :
                        continue 
                    q.append ((nr,nc))
                    grid [nr][nc] = "0"

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] =="1" :
                    grid [r][c] = "0"
                    bfs (r,c)
                    islands += 1

        return islands


        