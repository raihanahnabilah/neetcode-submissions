class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # I am at 0
        #pass, go to the next one
        # I am at 1
        # Change this to 0
        # Check left = 0
        # Check right = 1 -> add the index
        # Check down = 1 -> add the index
        
        totalRows = len(grid)
        totalCols = len(grid[0])
        res = 0

        for row in range(totalRows):
            for col in range(totalCols):
                if grid[row][col] == "0":
                    continue
                
                if grid[row][col] == "1":
                    queue = deque([(row, col)])

                    while queue:
                        currRow, currCol = queue.popleft()
                        grid[currRow][currCol] = "0"
                        for (dRow, dCol) in [(0,1), (0, -1), (1,0), (-1,0)]:
                            newRow = currRow + dRow
                            newCol = currCol + dCol
                            if newRow >= 0 and newRow < totalRows and newCol >= 0 and newCol < totalCols and grid[newRow][newCol] == "1":
                                queue.append((newRow, newCol))
                    res += 1
        
        return res






