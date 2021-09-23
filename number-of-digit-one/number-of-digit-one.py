class Solution:
    def countDigitOne(self, n: int) -> int:
        dp = [[[-1] * 2 for j in range(10)] for i in range(11)]
        n = str(n)[::-1]
        
        def DP(pos, ko, ch, dp):
            if pos == -1:
                return ko
            
            if dp[pos][ko][ch] != -1:
                return dp[pos][ko][ch]
            
            ret = 0
            if ch:
                for i in range(10):
                    ret += DP(pos - 1, ko + (i==1), ch, dp)
            else:
                for i in range(int(n[pos])):
                    ret += DP(pos - 1, ko + (i==1), 1, dp)
                ret += DP(pos - 1, ko + (n[pos] == '1'), 0, dp)
                
            dp[pos][ko][ch] = ret
            return ret

        return DP(len(n) - 1, 0, 0, dp)
