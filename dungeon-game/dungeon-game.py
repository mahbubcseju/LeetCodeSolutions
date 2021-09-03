class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n_row, n_col = len(dungeon), len(dungeon[0])
        ma = (n_row + n_col) * 1001
        ar = dungeon
        
        def isPossible(val):
            cop = [[ar[i][j] for j in range(n_col)] for i in range(n_row)]
            cop[0][0] += val
            for i in range(n_row):
                for j in range(n_col):
                    if i or j:
                        cop[i][j] += max(cop[i - 1][j] if i > 0 else -ma, cop[i][j-1] if j > 0 else -ma)
                    if cop[i][j] <= 0:
                        cop[i][j] = -(ma + 1000)
            return cop[n_row - 1][n_col - 1]
    
        lo, hi = 1, (n_row + n_col) * 1000
        ans = ma
        while lo <= hi:
            mid = (lo + hi) // 2
            if isPossible(mid) > 0:
                hi, ans = mid - 1, mid
            else:
                lo = mid + 1
        
        return ans