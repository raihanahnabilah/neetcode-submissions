class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cols = len(grid[0])
        rows = len(grid)
        res = 0
        visited = set()

        def bfs(row, col):
            queue = deque([[row, col]])
            visited.add((row, col))
            while queue:
                currRow, currCol = queue.popleft()
                for newRow, newCol in [(currRow + 1, currCol), (currRow - 1, currCol), (currRow, currCol + 1), (currRow, currCol - 1)]:
                    if newRow in range(rows) and newCol in range(cols) and (newRow, newCol) not in visited and grid[newRow][newCol] == "1":
                        queue.append([newRow, newCol])
                        visited.add((newRow, newCol))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row, col) not in visited:
                    bfs(row, col)
                    res += 1
        
        return res
