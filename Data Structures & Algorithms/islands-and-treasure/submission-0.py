from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        # Step 1: Add all gates (0s) to the queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        # Step 2: BFS from all gates simultaneously
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or
                    grid[nr][nc] != 2147483647):   # Skip if wall or visited
                    continue

                grid[nr][nc] = grid[row][col] + 1
                q.append((nr, nc))

        