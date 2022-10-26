class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[[0] * k for j in range(m)] for i in range(2)]
        mod = 1000000007
        
        flag = 0
        dp[0][0][0] = 1
        for i in range(n):
            flag ^= 1
            for j in range(m):
                for l in range(k):
                    dp[flag][j][l] = 0
                grid[i][j] %= k
                for l in range(k):
                    p = (l + grid[i][j])
                    if p >= k:
                        p -= k
                    dp[flag][j][p] = dp[flag^1][j][l] + dp[flag][j][p]
                    if dp[flag][j][p] >= mod:
                        dp[flag][j][p] -= mod
                    if j > 0:
                        dp[flag][j][p] = dp[flag][j-1][l] + dp[flag][j][p]
                        if dp[flag][j][p] >= mod:
                            dp[flag][j][p] -= mod
        
        return dp[flag][m-1][0]
