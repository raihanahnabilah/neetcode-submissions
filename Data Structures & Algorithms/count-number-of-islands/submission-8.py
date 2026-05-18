class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # time complexity: O(m*n) - we go through all values
        # space complexity: O(m*n) -> at most

        rows = len(grid)
        cols = len(grid[0])

        def bfs(row, col):
            queue = deque([(row, col)])
            grid[row][col] = "0"

            while queue:
                curr_row, curr_col = queue.popleft()

                for incr_row, incr_col in [(curr_row + 1, curr_col), (curr_row, curr_col + 1), (curr_row - 1, curr_col),(curr_row, curr_col - 1)]:
                    if incr_row >= 0 and incr_row < rows and incr_col >= 0 and incr_col < cols and  grid[incr_row][incr_col] == "1":
                        queue.append((incr_row, incr_col))
                        grid[incr_row][incr_col] = "0"


        # bfs
        # traverse through every single one
        # if it's 1, then we continue checking up, down, left right
        # if it's 0, we just skip and say good bye

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    res += 1
                    bfs(i, j)

        return res