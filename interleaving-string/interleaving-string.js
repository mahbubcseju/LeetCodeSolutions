/**
 * @param {string} s1
 * @param {string} s2
 * @param {string} s3
 * @return {boolean}
 */

var isInterLeave = function(s1, s2, s3, i, j, dp) {
    if(i === s1.length && j === s2.length){
        return true;
    }
    if(dp[i][j] != -1){
        return dp[i][j];
    }
    let res = false;
    let posi = i  + j;
    if (i < s1.length && s1[i] == s3[posi]) res |= isInterLeave(s1, s2, s3, i + 1, j, dp);
    if (j < s2.length && s2[j] == s3[posi]) res |= isInterLeave(s1, s2, s3,  i , j + 1, dp);
    return dp[i][j] = res;

}

var isInterleave = function(s1, s2, s3) {
    if(s1.length + s2.length != s3.length)return false;
    var dp = new Array(s1.length + 1).fill(-1).map(
        () => new Array(s2.length + 1).fill(-1)
    );
    return isInterLeave(s1, s2, s3, 0, 0, dp);
};