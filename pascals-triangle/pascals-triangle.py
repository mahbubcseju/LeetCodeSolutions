class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        res = [[1]]
        for i in range(1, numRows):
            res.append([0] * (i + 1))
            for j in range(i + 1):
                res[i][j] = ((res[i-1][j] if j < i else 0) + (res[i-1][j - 1] if (j-1) >= 0 else 0))
        return res
        