from collections import deque
class Solution:
    def hitBricks(self, grid, hits):
        self.dx = [0, 0, 1, -1]
        self.dy = [1, -1, 0, 0]
        res = []
        for hit in hits:
            if grid[hit[0]][hit[1]] == 0:
                res.append(0)
            else:
                count = 0
                grid[hit[0]][hit[1]] = 0
                count += self.bfs(grid, hit[0] - 1, hit[1], set([(hit[0], hit[1])]))
                count += self.bfs(grid, hit[0], hit[1] - 1, set([(hit[0], hit[1])]))
                count += self.bfs(grid, hit[0] + 1, hit[1], set([(hit[0], hit[1])]))
                count += self.bfs(grid, hit[0], hit[1] + 1, set([(hit[0], hit[1])]))
                res.append(count)

        return res

    def bfs(self, grid, x, y, seen):
        if not (0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1) or x == 0:
            return 0

        queue = deque([(x, y)])
        count = 0
        while queue:
            x, y = queue.popleft()
            if x == 0:
                return 0
            if (x, y) in seen:
                continue
            seen.add((x, y))
            count += 1
            for i in range(4):
                nx = x + self.dx[i]
                ny = y + self.dy[i]
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in seen and grid[nx][ny] == 1:

                    queue.append((nx, ny))

        for x, y in seen:
            grid[x][y] = 0
        return count

sol = Solution()
print(sol.hitBricks([[1,0,0,0],[1,1,0,0]], [[1,1],[1,0]]))

