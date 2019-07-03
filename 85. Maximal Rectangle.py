class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]: return 0
        m = len(matrix)
        n = len(matrix[0])
        h = [0] * (n + 1)
        res = 0

        for row in range(m):
            stack = []
            for i in range(n + 1):
                if i < n:
                    if matrix[row][i] == "1":
                        h[i] += 1
                    else:
                        h[i] = 0
                if not stack or h[stack[-1]] <= h[i]:
                    stack.append(i)
                else:
                    while stack:
                        if h[i] >= h[stack[-1]]: break
                        h1 = stack.pop()
                        if not stack:
                            area = h1 * i
                        else: area = h1 * (i - stack[-1] - 2)
                        res = max(area, res)
                    stack.append(i)
        return res

sol = Solution()
print(sol.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))