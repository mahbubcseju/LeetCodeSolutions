class Solution:
    def arrangeCoins(self, n: int) -> int:
        cnt, it = 0, 0
        while cnt <= n:
            it += 1
            cnt += it
        return it -1 