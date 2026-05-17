class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(row, col):
            queue = deque([])
            visited = set()

            queue.append([row, col])
            visited.add((row, col))
            currArea = 1

            while queue:
                currRow, currCol = queue.popleft()
                for nextRow, nextCol in [(currRow, currCol + 1), (currRow, currCol - 1), (currRow + 1, currCol), (currRow - 1, currCol)]:
                    if nextRow in range(rows) and nextCol in range(cols) and grid[nextRow][nextCol] == 1 and (nextRow, nextCol) not in visited:
                            queue.append([nextRow, nextCol])
                            visited.add((nextRow, nextCol))
                            currArea += 1
            return currArea

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    # traverse through it
                    currArea = bfs(row, col)
                    res = max(res, currArea)
        
        return res



        