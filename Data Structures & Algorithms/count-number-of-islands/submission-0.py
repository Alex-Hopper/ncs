class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        ROWS, COLS = len(grid), len(grid[0])
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    result += 1
                    self.dfs(grid, i, j)

        return result


    def dfs(self, grid, r, c):
        ROWS, COLS = len(grid), len(grid[0])
        if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == "0":
            return

        grid[r][c] = "0"

        self.dfs(grid, r + 1, c)
        self.dfs(grid, r - 1, c)
        self.dfs(grid, r, c + 1)
        self.dfs(grid, r, c - 1)