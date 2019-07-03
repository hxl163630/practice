class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        import heapq
        heap = [(2, start[0], start[1])]
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        while heap:
            step, curx, cury = heapq.heappop(heap)
            if maze[curx][cury] != 0 and maze[curx][cury] < step:
                continue
            maze[curx][cury] = step

            for i in range(4):
                newx, newy, step1 = self.getdest(dx[i], dy[i], curx, cury, maze)
                if step1 != 0:
                    heapq.heappush(heap, (step + step1, newx, newy))
        if maze[destination[0]][destination[1]] == 0:
            return -1
        return maze[destination[0]][destination[1]] - 1

    def getdest(self, dx, dy, x, y, maze):
        step = 0
        while 0 <= x + dx < len(maze) and 0 <= y + dy < len(maze[0]) and maze[x + dx][y + dy] != 1:
            step += 1
            x += dx
            y += dy
        return x, y, step


sol = Solution()
sol.shortestDistance([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],
[0,4],
[4,4])