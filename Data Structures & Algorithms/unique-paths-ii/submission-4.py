class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        prevRow = [0] * n

        if m == 1 and n == 1:
            return 1 if obstacleGrid[0][0] == 0 else 0

        for row in range(m - 1, -1, -1):
            curRow = [0] * n
            # curRow[n - 1] = prevRow[n - 1] if row == (m - 1) else 1
            if row + 1 == m: # goal spot
                curRow[n - 1] = 1
            else:
                curRow[n - 1] = prevRow[n - 1] if not obstacleGrid[row][n - 1] else 0
            

            for col in range(n - 2, -1, -1):
                curRow[col] = curRow[col + 1] + prevRow[col]
                # print(row, col, m, n)
                if obstacleGrid[row][col] == 1:
                    curRow[col] = 0

            prevRow = curRow

        return prevRow[0]
