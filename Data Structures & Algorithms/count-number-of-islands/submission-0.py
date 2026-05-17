class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # I think for this we can do breadth first search?
        # I really forgot how this is done

        if grid == [[]]:
            return 0
        
        totalCols = len(grid[0])
        totalRows = len(grid)
        islands = 0

        def bfs(rootRow, rootCol):
            queue = deque([(rootRow, rootCol)])
            grid[rootRow][rootCol] = "0"

            while queue:
                i, j = queue.popleft()

                # need to check the surrounding
                for (row, col) in [(0,1), (0,-1), (1,0), (-1,0)]:
                    print("Checking irow jcol", i+row, j+col)
                    if i+row < 0 or j+col < 0 or i+row >= totalRows or j+col >= totalCols or grid[i+row][j+col] == "0":
                        continue
                    queue.append((i+row, j+col))
                    grid[i+row][j+col] = "0"

        for i in range(totalRows):
            for j in range(totalCols):
                if grid[i][j] == "1":
                    bfs(i, j)
                    islands += 1

        return islands

