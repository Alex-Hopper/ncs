class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        queue = deque()
        # add all rotten fruits to queue.
        ROWS, COLS = len(grid), len(grid[0])
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append((i, j))
        
        minutes = 0
        remaining = sum(row.count(1) for row in grid)
        prev = remaining + 1
        while queue and remaining:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                neighbors = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in neighbors:
                    if min(r + dr, c + dc) < 0 or r + dr == ROWS or c + dc == COLS \
                        or grid[r + dr][c + dc] != 1:
                        continue
                    grid[r + dr][c + dc] = 2
                    remaining -= 1
                    queue.append((r + dr, c + dc))

            # if remaining == prev:
            #     return -1

            minutes += 1



        return minutes if remaining == 0 else -1

        