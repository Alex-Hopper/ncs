class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = {}

        def dfs(m, n):
            if m == 1 or n == 1:
                return 1
            
            if (m, n) in memo:
                return memo[(m, n)]

            memo[(m, n)] = dfs(m - 1, n) + dfs(m, n - 1)
            return memo[(m, n)]
        
        return dfs(m, n)