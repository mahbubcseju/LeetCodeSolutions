class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def Up(i, j, board):
            return any([True if board[k][j] == 'Q' else False for k in range(i)])
        def left_cross(i, j, board):
            return any([True if board[i - k][j - k] == 'Q' else False for k in range(min(i,j) + 1)])
        def right_cross(i, j, board):
            return any([True if board[i - k][j + k] == 'Q' else False for k in range(min(i + 1, n -j) )])
        
        def solve_N_queens(pos: int, board: List[str], res: List[List[str]]):
            if pos == n:
                res.append([board[i][:] for i in range(n)])
                return
            for j in range(n):
                if not Up(pos, j, board) and not left_cross(pos, j, board) and not right_cross(pos, j, board):
                    # print(board, pos, j, Up(pos, j, board))
                    board[pos] = board[pos][:j] + 'Q' + board[pos][j + 1:]
                    solve_N_queens(pos + 1, board, res)
                    board[pos] = board[pos][:j] + '.' + board[pos][j + 1:]
            
        board = [''.join(['.' for j in range(n)]) for i in range(n)]
        res = []
        solve_N_queens(0, board, res)
        
        return res