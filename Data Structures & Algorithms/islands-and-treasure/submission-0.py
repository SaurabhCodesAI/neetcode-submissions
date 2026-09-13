from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        inf = 2147483647

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row, col))

        while queue:
            row, col = queue.popleft()

            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change

                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if grid[new_row][new_col] == inf:
                        grid[new_row][new_col] = grid[row][col] + 1
                        queue.append((new_row, new_col))