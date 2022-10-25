class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        max_height = max([x[1] for x in envelopes]) + 2
        dp = [0 for i in range(max_height * 4)]
        
        def build(n, s, e, ind, value):
            if s == e:
                dp[n] = value
                return
            mid = ( s + e) // 2
            left = n * 2
            if ind <= mid:
                build(left, s, mid, ind, value)
            else:
                build(left + 1, mid + 1, e, ind, value)
            dp[n] = max(dp[left], dp[left + 1])
        
        def query(n, s, e, st, en):
            if s == st and e == en:
                return dp[n]
            mid = (s + e) // 2
            left = n * 2
            if mid >= en:
                return query(left, s, mid, st, en)
            elif mid < st:
                return query(left + 1, mid + 1, e, st, en)
            else:
                return max(query(left, s, mid, st, mid), query(left + 1, mid + 1, e, mid + 1, en))
        
        envelopes = sorted(envelopes, reverse=True)
        result = []
        for ind, item in enumerate(envelopes):
            if ind > 0 and envelopes[ind-1][0] > item[0]:
                for ind_1 in range(ind - 1, -1, -1):
                    if envelopes[ind_1][0] != envelopes[ind -1][0]:
                        break
                    build(1, 1, max_height, envelopes[ind_1][1], result[ind_1])
            # print(query(1, 1, max_height, envelopes[ind][1] + 1, max_height), envelopes[ind][1] + 1, max_height)
            result.append(query(1, 1, max_height, envelopes[ind][1] + 1, max_height) + 1)

        return max(result)
