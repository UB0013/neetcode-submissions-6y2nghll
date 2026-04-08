class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        #res = 0 

        def bfs (r,c) :
            res = 1

            q =  collections.deque()
            q.append((r,c))

            while q : 
                r, c  = q.popleft()
                for mr , mc in directions : 
                    nr , nc = mr +r , mc +c 
                    if (nr < 0 or nc < 0 or nr>= rows 
                    or nc >=cols or grid [nr] [nc] == 0 ) :
                        continue
                    grid [nr][nc] = 0 
                    q.append((nr,nc))
                    res += 1
            return res 
                    



        area =0 
        for r in range(rows):
            for c in range (cols):
                if grid [r][c] ==1 :
                    grid [r][c] = 0 
                    area = max(area, bfs(r,c))
                    bfs(r,c)

        return area








        