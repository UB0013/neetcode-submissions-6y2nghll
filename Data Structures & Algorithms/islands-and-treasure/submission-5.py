class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        path = set ()
        q = deque ()
        rows = len (grid)
        cols = len (grid[0])
        directions = [[0,1],[0,-1],[-1,0],[1,0]]

        for r in range (rows):
            for c in range ( cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    path.add ((r,c))
        
        while q : 
            print(16)
            lenq = len(q) 
            for i in range (lenq ): 
                r, c = q.popleft()
                print (r,c)
                for mr, mc in directions :
                    print(23)
                    nr = r+mr 
                    nc = c+mc
                    if nr >= 0 and nc >=0 and nr < rows and nc < cols and  grid[nr][nc] == 2147483647: 
                        print(26)
                        grid[nr][nc] = grid[r][c]+1 
                        q.append((nr,nc))
                    
        






        

                



        