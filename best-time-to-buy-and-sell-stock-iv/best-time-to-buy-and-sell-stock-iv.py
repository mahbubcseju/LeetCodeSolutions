class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        le, k = len(prices), k * 2
        dp = [[-100000000] * (k + 1) for i in range(le + 1)]
        dp[0][0] = 0
        
        for i in range(1, le + 1):
            dp[i][0] = 0
            for j in range(1, k + 1):
                dp[i][j] = dp[i-1][j - 1] + ((-1 if (j % 2) else 1) * prices[i - 1])
                dp[i][j] = max(dp[i][j], dp[i-1][j])
                
        return max(dp[le])
                