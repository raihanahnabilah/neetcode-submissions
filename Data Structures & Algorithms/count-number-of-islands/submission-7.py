class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def findIsland(i, j):            
            queue = deque([])
            queue.append((i, j))
            while queue:
                curr_row, curr_col = queue.popleft()
                grid[curr_row][curr_col] = "0" # basically marking as visited
                for row, col in [(curr_row+1, curr_col), (curr_row-1, curr_col), (curr_row, curr_col+1), (curr_row, curr_col-1)]:
                    if row in range(rows) and col in range(cols) and grid[row][col] == "1":
                        queue.append((row, col))
            
        rows = len(grid)
        cols = len(grid[0])

        islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    findIsland(i, j)
                    islands += 1
        
        return islands









