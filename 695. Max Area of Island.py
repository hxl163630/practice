class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        output = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                visited = self.compute(grid, i, j,[])
                output = max(output, len(visited))
                for i, j in visited:
                    grid[i][j] = 0
        return output

    def compute(self, grid, i, j, visited=[]):
        if [i, j] not in visited and grid[i][j] == 1:
            visited.append([i, j])
            if i - 1 >= 0: visited = self.compute(grid, i - 1, j, visited)
            if j - 1 >= 0: visited = self.compute(grid, i, j - 1, visited)
            if i + 1 <= len(grid) - 1: visited = self.compute(grid, i + 1, j, visited)
            if j + 1 <= len(grid[0]) - 1: visited = self.compute(grid, i, j + 1, visited)
            return visited



        else:
            return visited


sol = Solution()
print(sol.maxAreaOfIsland([[0]]))