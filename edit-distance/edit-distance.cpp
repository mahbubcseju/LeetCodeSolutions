class Solution {
public:
    
    int inf=2e9;
    
    int minDistance(string w1, string w2) {
        
        int n=w1.size();
        
        int m=w2.size();
        
        int dp[n+2][m+2];
        
        
        
        for(int i=0;i<=n;i++)
        {
            
            for(int j=0;j<=m;j++)
            {
                dp[i][j]=inf;
            }
        }
        
        dp[0][0]=0;
        
        for(int j=1;j<=m;j++)dp[0][j]=j;
        
        for(int j=1;j<=n;j++)dp[j][0]=j;
        
        
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=m;j++)
            {
                if(w1[i-1]==w2[j-1])
                {
                    dp[i][j]=min(dp[i][j],dp[i-1][j-1]);
                    
                }
                 dp[i][j]=min(dp[i][j],dp[i-1][j-1]+1);
                dp[i][j]=min(dp[i][j],dp[i][j-1]+1);
                
                dp[i][j]=min(dp[i][j],1+dp[i-1][j]);
                
                
                
                
            }
        }
        return dp[n][m];
        
    }
};