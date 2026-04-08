from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return

        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()

        # Step 1: Collect all gates (value = 0)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        # Step 2: BFS helper
        def bfs():
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    # Skip invalid cells or visited ones
                    if (nr < 0 or nr >= rows or
                        nc < 0 or nc >= cols or
                        grid[nr][nc] != 2147483647):
                        continue

                    # Update distance and enqueue the new cell
                    grid[nr][nc] = grid[row][col] + 1
                    q.append((nr, nc))

        # Step 3: Run BFS from all gates
        bfs()
