from collections import deque
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        move = {'top': (-1, 0), 'bottom': (1,0), 'left': (0,-1), 'right': (0, 1)}
        ROW, COL = len(board), len(board[0])
        answer = False
        def dfs(start_idx, depth, subset):
            nonlocal answer
            
            if len(subset) == len(word):
                answer = True
                return
            
            for k,v in move.items():
                cur_row, cur_col = start_idx[0], start_idx[1]
                next_row, next_col = cur_row + v[0], cur_col + v[1]
                
                if 0 <= next_row < ROW and 0 <= next_col < COL:
                    if board[next_row][next_col] == word[depth]:
                        tmp = board[next_row][next_col]
                        board[next_row][next_col] = '#'
                        dfs((next_row, next_col), depth+1, subset + word[depth])
                        board[next_row][next_col] = tmp
                        
        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == word[0]:
                    tmp = board[i][j]
                    board[i][j] = '#'                
                    dfs((i,j), 1, word[0])
                    board[i][j] = tmp
                    
                if answer:
                    return True
                
        return answer
