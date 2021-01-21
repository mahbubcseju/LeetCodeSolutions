class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        
        row_flag, col_flag = 1, 1
        for i in range(n):
            if matrix[i][0] == 0:
                col_flag = 0
                
        for i in range(m):
            if matrix[0][i] == 0:
                row_flag = 0
                
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        for i in range(n):
            matrix[i][0] *= col_flag
                
        for i in range(m):
            matrix[0][i] *= row_flag
            
        