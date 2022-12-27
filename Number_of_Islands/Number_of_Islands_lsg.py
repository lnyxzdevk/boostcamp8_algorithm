from collections import deque

class Solution:
    def bfs(self, init_pos):
        check = set()
        next_move = deque([init_pos])
        while next_move:
            pos = next_move.popleft()
            for step in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dx, dy = step
                x, y = pos[0] + dx, pos[1] + dy
                if x >= 0 and y >= 0 and x < len(self.grid[0]) and y < len(self.grid) \
                and not (x, y) in check and self.grid[y][x] == '1':
                    check.add((x, y))
                    next_move.append((x, y))

        self.global_check |= check
        self.answer += 1

    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.answer = 0
        self.global_check = set()
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val == '1' and not (x, y) in self.global_check:
                    self.bfs((x, y))
        return self.answer
