class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
#         dp = [[0] * (n + 1) for i in range(n + 1) ]
        
#         for i in range(n):
#             for j in range(i, n):
#                 if s[i: j + 1] in wordDict:
#                     dp[i][j] = 1
        
        ans = []
        for i in range(1<<n):
            word = ''
            words = []
            flag = 0
            for j in range(n):
                word += s[j]
                if (i & (1 << j)) > 0:
                    if word not in wordDict:
                        flag = 1
                        break;
                    else:
                        words.append(word)
                        word = ''

            if not flag and not word:
                ans.append(' '.join(words))
                    
        return ans
            
        