class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len (heights)
        cols = len (heights[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        visitedpacific = [[False] * cols for i in range(rows)]
        visitedatlantic = [[False] * cols for i in range(rows)]

        pacific = []
        atlantic = [] 

        for c in range(cols) : 
            pacific.append((0,c))
            atlantic.append((rows-1,c))
        for r in range (rows) : 
            pacific.append((r,0))
            atlantic.append((r,cols-1))
        
        def bfs(ocean, visited) :

            q = deque(ocean)

            while q : 
                r, c = q.popleft()
                visited[r][c] = True
                for mr, mc in directions: 
                    nr = r+mr
                    nc = c + mc

                    if (nr < 0 or nc < 0 or nr >=rows or nc >= cols or visited[nr][nc] == True or heights[nr][nc]< heights[r][c]) :
                        continue 
                    q.append((nr,nc))
        bfs (pacific,visitedpacific)
        bfs(atlantic,visitedatlantic)

        res= []

        for r in range (rows):
            for c in range (cols): 
                if visitedpacific[r][c] and  visitedatlantic[r][c] : 
                    res.append([r,c])
        return res

                   






        