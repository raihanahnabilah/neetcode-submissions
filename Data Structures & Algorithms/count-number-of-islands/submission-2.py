class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # I am at 0
        #pass, go to the next one
        # I am at 1
        # Change this to 0
        # Check left = 0
        # Check right = 1 -> add the index
        # Check down = 1 -> add the index

        # This is BFS
        
        totalRows = len(grid)
        totalCols = len(grid[0])
        res = 0

        def dfs(row, col):
            nonlocal res

            if row < 0 or row >= totalRows or col < 0 or col >= totalCols or grid[row][col] == "0":
                return 

            grid[row][col] = "0"

            for (dRow, dCol) in [(0,1), (0, -1), (1,0), (-1,0)]:
                newRow = row + dRow
                newCol = col + dCol
                dfs(newRow, newCol)

        for row in range(totalRows):
            for col in range(totalCols):
                if grid[row][col] == "1":
                    dfs(row, col)
                    res += 1
    
        return res






