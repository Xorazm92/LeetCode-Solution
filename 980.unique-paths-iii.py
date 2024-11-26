class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def nimadir(i, j, empty):
            if not (0 <= i < rows and 0 <= j < cols) or grid[i][j] < 0:
                return
            if (i,j) == end and empty == 0:
                self.paths += 1
                return 
            grid[i][j] = -2
            for ni, nj in [(i+1,j), (i-1,j), (i,j-1), (i, j+1)]:
                nimadir(ni, nj, empty-1)
            grid[i][j] = 0

        rows = len(grid)
        cols = len(grid[0])

        empty = 0
        start = None
        end = None

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    start = (i,j)
                if grid[i][j] != -1:
                    empty += 1
                if grid[i][j] == 2:
                    end = (i, j)

        self.paths = 0
        nimadir(start[0], start[1], empty - 1)
        return self.paths