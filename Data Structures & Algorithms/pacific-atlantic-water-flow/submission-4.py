class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows = len (heights) 
        cols = len(heights[0])
        directions = [ (0,1),(1,0),(-1,0),(0,-1)]
        pac = [[False] * cols for i in range (rows)]
        atl = [[False] * cols for i in range (rows)]

        pacific =[]
        atlantic =[]

        for c in range (cols):
            pacific.append((0,c))
            atlantic.append ((rows-1,c))
        for r in range (rows):
            pacific.append((r,0))
            atlantic.append((r,cols-1))
        
        def bfs (source, ocean):
            q = deque(source)
            while q:
                
                r, c = q.popleft()
                if ocean[r][c]:
                    continue  
                ocean [r][c] = True 
                for mr, mc in directions :
                    nr  = mr + r 
                    nc =  mc + c
                    if (nr < 0 or nc < 0 or nr >= rows or nc >=cols 
                    or heights[nr][nc] < heights [r][c] or ocean[nr][nc]) :
                        continue 
                    q.append ((nr,nc))

        bfs(pacific, pac)
        bfs(atlantic, atl)

        
        res = []
                    

        for r in range(rows):
            for c in range(cols): 
                if pac [r][c] and atl[r][c]:
                    res.append([r,c])
        return res
                





       

        