from collections import deque


class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """

        def getIndex(curIndex, N):
            x = N - 1 - (curIndex - 1) // N
            if ((curIndex - 1) // N) % 2 == 0:
                y = (curIndex - 1) % N
            else:
                y = N - 1 - (curIndex - 1) % N
            return x, y

        queue = deque([(1, 0)])
        visited = set([1])
        N = len(board)
        while queue:
            curIndex, step = queue.popleft()
            for i in range(curIndex + 1, curIndex + 7):
                x, y = getIndex(i, N)
                if board[x][y] > 0:
                    i = board[x][y]
                if i == N * N:
                    return step + 1
                if i not in visited:
                    visited.add(i)
                    queue.append((i, step + 1))
        return -1

sol = Solution()
print(sol.snakesAndLadders([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]))