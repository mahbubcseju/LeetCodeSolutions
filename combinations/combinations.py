class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        from functools import reduce
        ans = []
        for i in range(1, (1 << n)):
            val = reduce(lambda x, y: x + ([y + 1] if (i & (1 << y)) > 0 else []), range(0, 20), [])
            if len(val) == k:
                ans.append(val)
        return ans