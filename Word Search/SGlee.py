class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x, y, subword):
            # print(x, y, result, visit)
            if subword == word:
                return True
                
            for dx, dy in move:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= len(board[0]) \
                    or ny < 0 or ny >= len(board):
                    continue
                pos = len(subword)
                next_subword = subword + board[ny][nx]
                if visit[ny][nx] == 0 and board[ny][nx] == word[pos] \
                    and (nx, ny, next_subword) not in visit_path:
                    visit[ny][nx] = 1
                    visit_path.add(next_subword)
                    if dfs(nx, ny, next_subword):
                        return True
                    visit[ny][nx] = 0
                else:
                    continue

            return False
        
        visit = [[0]*len(board[0]) for _ in range(len(board))]
        visit_path = set()
        move = [(1, 0), (0, 1), (-1 ,0), (0, -1)]

        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == word[0]:
                    visit[y][x] = 1
                    if dfs(x, y, board[y][x]):
                        print(len(visit_path))
                        return True
                    visit[y][x] = 0
        print(len(visit_path))
        return False
    
