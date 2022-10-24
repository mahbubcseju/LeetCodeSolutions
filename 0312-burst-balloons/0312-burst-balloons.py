class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        length = len(nums) 
        dp = [[0 for j in range(length)] for i in range(length)]
        
        
        for i in range(length - 1 , -1, -1):
            for j in range(i + 2, length):
                for k in range(i + 1, j):
                    dp[i][j] = max(nums[i] * nums[j] * nums[k] + dp[i][k] + dp[k][j], dp[i][j])
        
        return dp[0][length-1]