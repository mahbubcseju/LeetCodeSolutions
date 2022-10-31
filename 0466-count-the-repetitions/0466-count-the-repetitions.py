class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        
        l1 = len(s1)
        l2 = len(s2)
        dp = [[(l1, l2) for j in range(l2)] for i in range(l1)]
        
        
        for i in range(l1):
            for j in range(l2):
                k, m = j, i
                
                while k < l2 and m < l1:
                    if s2[k] == s1[m]:
                        k += 1
                        m += 1
                    else:
                        m += 1
                dp[i][j] = (m, k)
                # print(i, j, m, k)
        
        flag = 0
        k, cnt = 1, 0
        ptr_s1, ptr_s2 = 0, 0
        while k <= n1:
            te_ptr_s1, te_ptr_s2 = ptr_s1, ptr_s2
            ptr_s1 = dp[te_ptr_s1][te_ptr_s2][0]
            ptr_s2 = dp[te_ptr_s1][te_ptr_s2][1]
            
            if ptr_s1 == l1 and ptr_s2 == l2:
                koto = n1 // k
                cnt = (cnt + 1) * koto - 1
                k = k * koto
            
            if ptr_s1 == l1:
                ptr_s1 = 0
                k += 1
            if ptr_s2 == l2:
                cnt += 1
                ptr_s2 = 0
#             print(ptr_s1, ptr_s2, k, cnt)
        
#         print(cnt)
        return cnt  // n2
