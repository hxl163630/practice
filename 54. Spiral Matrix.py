class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        k = 0
        m = len(matrix)
        n = len(matrix[0])
        output = []
        while m - k >= k and n - k >= k:
            for i in range(k, n - k):
                output.append(matrix[k][i])
            for i in range(k + 1, m - k):
                output.append(matrix[i][n - k - 1])
            for i in range(n - k - 2, k - 1, -1):
                if k + 1 == m - k: continue
                output.append(matrix[m - k - 1][i])
            for i in range(m - k - 2, k, -1):
                if n-k-2 == k-1: continue
                output.append(matrix[i][k])

            k += 1
        return output

sol = Solution()
print(sol.spiralOrder([[1,2,3],
                       [4,5,6]
                       ]))