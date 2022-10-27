class Solution {
public:
    int splitArray(vector<int>& nums, int k) {
        int len = nums.size();
        int dp[len + 1][ k + 1];
        for(int i = 0; i  <= len; i++) {
            for(int j = 0; j <= k; j++)dp[i][j]= 2000000000;
        }
        dp[0][0] = 0;
        
        for(int i = 1; i <= len; i++) {
            int sum = 0;
            for(int l = i ; l <= len; l++) {
                sum += nums[l-1];
                for(int j = 1; j <= k; j++){
                    dp[l][j] = min(dp[l][j], max(dp[i - 1][j - 1], sum));
                }
            }
            
        }
        return dp[len][k];
    }
};