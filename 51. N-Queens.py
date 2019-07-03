class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        dic = []
        output = []
        def isValid(i, j):
            for pnt in dic:
                if i == pnt[0] or j == pnt[1]:
                    return False

            k = 1
            while k < n:
                if [i - k, j - k] in dic:
                    return False
                if [i + k, j + k] in dic:
                    return False
                if [i + k, j - k] in dic:
                    return False
                if [i - k, j + k] in dic:
                    return False
                k += 1
            return True


        def helper(dic, row):
            if row == n:
                output.append(dic[:])
                return
            for col in range(n):
                if(isValid(row, col)):
                    dic.append([row, col])
                    helper(dic, row + 1)
                    del dic[-1]




        helper(dic, 0)
        return [ ["."*pnt[1] + "Q" + "."*(n-pnt[1]-1) for pnt in pnts] for pnts in output]

sol = Solution()
print(sol.solveNQueens(4))