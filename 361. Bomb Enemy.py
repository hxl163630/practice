class Solution(object):
    def maxKilledEnemies(self, grid):
        if len(grid) == 0:
            return 0
        max_hits = 0
        nums = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]

        # From Left
        for i in range(len(grid)):
            row_hits = 0
            for j in range(len(grid[0])):
                if grid[i][j] == 'E':
                    row_hits += 1
                elif grid[i][j] == 'W':
                    row_hits = 0
                else:
                    nums[i][j] = row_hits

        # From Right
        for i in range(len(grid)):
            row_hits = 0
            for j in range(len(grid[0]) - 1, -1, -1):
                if grid[i][j] == 'W':
                    row_hits = 0
                elif grid[i][j] == 'E':
                    row_hits += 1
                else:
                    nums[i][j] += row_hits

        for i in range(len(nums[0])):
            col_hits = 0
            for col in range(len(nums)):
                if grid[col][i] == 'E':
                    col_hits += 1
                elif grid[col][i] == 'W':
                    col_hits = 0
                else:
                    nums[col][i] += col_hits

        for i in range(len(nums[0])):
            col_hits = 0
            for col in range(len(nums) - 1, -1, -1):
                if grid[col][i] == 'E':
                    col_hits += 1
                elif grid[col][i] == 'W':
                    col_hits = 0
                else:
                    nums[col][i] += col_hits
                    max_hits = max(max_hits, nums[col][i])


sol = Solution()
sol.maxKilledEnemies([["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]])