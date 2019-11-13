from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False

        # binary search
        l, r = 0, m * n - 1
        while l <= r:
            mid = (l + r) // 2
            i = mid // n
            j = mid % n
            if target == matrix[i][j]:
                return True
            if target < matrix[i][j]:
                r = m - 1
            else:
                l = m + 1
        return False

sol = Solution()
sol.searchMatrix([[1]]
,0)