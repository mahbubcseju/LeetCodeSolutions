class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt = 0
        for i in range(1, n + 1):
            x = i
            while x % 5 == 0:
                cnt += 1
                x //= 5
        return cnt
            