class Solution(object):
    def shortestDistance(self, maze, start, destination):

        from collections import deque
        queue = deque([start])
        dxdy = [0, 1, 0, -1, 0]
        while queue:
            curx, cury = queue.popleft()
            if curx == destination[0] and cury == destination[1]:
                return True
            maze[curx][cury] == 2
            for i in range(4):
                destx, desty = self.getdest(dxdy[i], dxdy[i + 1], curx, cury, maze)

                if maze[destx][desty] != 2 and not (curx == destx and cury == desty):
                    queue.append([destx, desty])
        return False

    def getdest(self, dx, dy, x, y, maze):
        while 0 <= x + dx < len(maze) and 0 <= y + dy < len(maze[0]) and maze[x + dx][y + dy] != 1:
            x += dx
            y += dy
        return x, y


sol = Solution()
sol.shortestDistance([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],
[0,4],
[4,4])