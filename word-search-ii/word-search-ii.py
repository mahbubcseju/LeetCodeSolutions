class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rown, coln = len(board), len(board[0])
        vis = [[0] * coln for i in range(rown)]
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        def test_back_tracking(x, y, vis, st, ind):
            if len(st) == ind + 1:
                return True
            for i in range(4):
                x1 = dx[i] + x
                y1 = dy[i] + y
                if 0 <= x1 < rown and 0 <= y1 < coln and not vis[x1][y1] and  board[x1][y1] == st[ind + 1]:
                    vis[x1][y1] = 1
                    ans = test_back_tracking(x1, y1, vis, st, ind + 1)
                    vis[x1][y1] = 0
                    if ans:
                        return True
            return False
        
        def call_for_single_string(cur):
            for i in range(len(cur)):
                if cur[i] not in character_sets:
                    return False
    
            for i in range(rown):
                for j in range(coln):
                    if board[i][j] != cur[0]:
                        continue
                    vis[i][j] = 1
                    if test_back_tracking(i, j, vis, cur, 0):
                        vis[i][j] = 0
                        return True
                    vis[i][j] = 0
            return False
        
        character_sets = {''}
        for i in range(rown):
            for j in range(coln):
                character_sets.add(board[i][j])
        print(character_sets)
        
        result = []   
        for word in words:
            if call_for_single_string(word):
                result.append(word)
    
        return result
            