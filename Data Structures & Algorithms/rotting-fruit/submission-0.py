class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q= collections.deque ()
        fresh = 0 
        time = 0 
        rows =len(grid) 
        cols = len(grid[0])

        for r in range(rows):
            for c in range (cols):
                if grid [r][c] == 2 :
                    q.append ((r,c))
                if grid[r][c] == 1 :
                    fresh += 1 
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        while q and fresh > 0 : 
            for i in range (len(q)):
                r, c = q.popleft()
                for mr , mc in directions : 
                    nr, nc = r + mr, c + mc 
                    if nr <0 or nc<0 or nr >= rows or nc >=cols or grid [nr][nc] !=1 :
                        continue 
                    # rot the fresh orange
                    grid[nr][nc] = 2
                    q.append((nr, nc)) 
                    fresh -= 1
            time += 1
        
        if fresh  == 0 :
            return time 
        else :
            return -1 
                


        