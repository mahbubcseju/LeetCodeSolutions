/**
 * @param {string} s
 * @return {number}
 */
var minCut = function(s) {
    var len = s.length;
    var dp = new Array(len + 1).fill(0).map(() => new Array(len + 1).fill(0));
    
    for(let i = len - 1; i >= 0; i--){
        dp[i][i] = 1;
        if(i + 1 < len && s[i] == s[i + 1]) {
            dp[i][i + 1] = 1;
        }
        for(let j = i + 2; j < len; j++){
            if(s[i] == s[j]) {
                dp[i][j] = (dp[i + 1][j - 1]? 1: 0);
            }
        }
    }
    
    var DP = new Array(len + 1).fill(len + 1);
    DP[0] = 0;
    for(let i = 1; i<= len; i++){
        for(let j = i; j >= 1; j--){
            if(dp[j - 1][i-1] == 1){
                DP[i] = Math.min(DP[j-1] + 1, DP[i]);
            }
        }
    }
    
    return DP[len] - 1;
};