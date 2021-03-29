class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row_length = len(board)
        if row_length == 0:
            return board
        col_length = len(board[0])
        
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        
        vis = [[-1] * col_length for i in range(row_length)]
        
        def is_outside(x, y):
            if x == -1 or x == row_length:
                return True
            if y == -1 or y == col_length:
                return True
            print(x, y)
            if board[x][y] == 'X' or vis[x][y] != -1:
                return False
            vis[x][y] = 1
            
            res = False
            for j in range(4):
                x1, y1 = x + dx[j], y + dy[j]
                print(x, y, x1, y1)
                if is_outside(x1, y1) :
                    res |= True
    
            return res
    
        def fill_inside(x, y):
            board[x][y] = 'X'
            for j in range(4):
                x1, y1 = x + dx[j], y + dy[j]
                if x1 == -1 or x1 == row_length:
                    continue
                if y1 == -1 or y1 == col_length:
                    continue
                if board[x1][y1] == 'X':
                    continue
                fill_inside(x1, y1)
        
        for i in range(row_length):
            for j in range(col_length):
                if vis[i][j] == -1 and board[i][j] == 'O':
                    print(i, j)
                    if not is_outside(i, j):
                        fill_inside(i, j)
            
        return board
                        
            