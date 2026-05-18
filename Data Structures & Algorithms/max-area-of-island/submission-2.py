class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        maxRes = 0

        def bfs(row, col):
            queue = deque([(row, col)])
            grid[row][col] = 0
            counter = 1

            while queue:
                curr_row, curr_col = queue.popleft()

                for incr_row, incr_col in [(curr_row+1, curr_col), (curr_row, curr_col+1), (curr_row-1, curr_col), (curr_row, curr_col-1)]:
                    if incr_row in range(rows) and incr_col in range(cols) and grid[incr_row][incr_col] == 1:
                        queue.append((incr_row, incr_col))
                        grid[incr_row][incr_col] = 0
                        counter += 1
            return counter

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = bfs(i, j)
                    maxRes = max(res, maxRes)
        
        return maxRes


