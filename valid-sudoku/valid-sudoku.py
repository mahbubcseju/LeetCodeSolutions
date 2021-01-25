class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row_col = [[[0]  * 10  for j in range(9)]for i in range(2)]
        sub_matrix = [[[0] * 10 for j in range(3) ] for i in range(3)]
        
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if col.isdigit():
                    val = int(col)
                    row_col[0][i][val] += 1
                    row_col[1][j][val] += 1
                    sub_matrix[i // 3][j // 3][val] += 1
                    if row_col[0][i][val] > 1 or row_col[1][j][val] > 1 or   sub_matrix[i // 3][j // 3][val] > 1:
                        return False
        return True