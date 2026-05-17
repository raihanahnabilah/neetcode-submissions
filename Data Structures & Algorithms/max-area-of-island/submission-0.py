class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        totalCols = len(grid[0])
        totalRows = len(grid)
        maxArea = 0

        def bfs(rootRow, rootCol):
            queue = deque([(rootRow, rootCol)])
            grid[rootRow][rootCol] = 0
            initialArea = 1

            while queue:
                row, col = queue.popleft()

                for (r, c) in [(0,1), (0,-1), (1,0), (-1,0)]:
                    if row+r < 0 or col+c < 0 or row+r >= totalRows or col+c >= totalCols or grid[row+r][col+c] == 0:
                        continue
                    queue.append((row+r, col+c))
                    grid[row+r][col+c] = 0
                    initialArea += 1

            return initialArea

        for i in range(totalRows):
            for j in range(totalCols):
                if grid[i][j] == 1:
                    currentArea = bfs(i, j)
                    print("Checking currentArea", currentArea)
                    maxArea = max(maxArea, currentArea)
        
        return maxArea
