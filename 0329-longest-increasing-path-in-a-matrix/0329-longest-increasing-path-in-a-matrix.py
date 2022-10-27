class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])
        
        nums = []
        for i in range(n):
            for j in range(m):
                nums.append((matrix[i][j], i, j))
        nums = sorted(nums)
        
        dx = [-1, 1 , 0, 0]
        dy = [0, 0, 1, -1]
        dp = [[0] * m for i in range(n)]
        for item in nums:
            val, x, y = item
            dp[x][y] = 1
            for x1, y1 in zip(dx, dy):
                x2 = x + x1
                y2 = y + y1
                if 0 <= x2 < n and 0 <= y2 < m and matrix[x2][y2] < matrix[x][y]:
                    dp[x][y] = max(dp[x][y], 1 + dp[x2][y2])
        
        return max([j  for x in dp for j in x])
