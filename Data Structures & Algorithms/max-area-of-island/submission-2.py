class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len (grid)
        cols =len(grid[0])
        directions =  [[1,0],[-1,0],[0,1],[0,-1]]
        res = 0
        area =0  
        def dfs (r,c): 
            nonlocal area
            if not grid :
                return 0 
            grid[r][c] = 0 
            area += 1
            for mr , mc in directions : 
                nr = r + mr 
                nc = c + mc 
                if nr >=0 and nc >= 0 and nr < rows and nc < cols and grid [nr][nc] ==1 :
                    dfs (nr,nc)
            return area 

        
       



        for r in range (rows) :
            for c in range (cols) : 
                if grid [r][c] == 1:
                    area = 0 
                    area = dfs (r,c)
                    res = max(res, area)
        
        return res
                    

     