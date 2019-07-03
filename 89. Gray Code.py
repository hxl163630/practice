class Solution:
    def grayCode(self, n):
        maxval = 2 ** n - 1
        self.res = []
        def dfs(n, cur, maxval):
            if len(cur) == maxval + 1:
                self.res= cur[:]
                return
            if self.res != []:
                return
            cand = [1 << i ^ cur[-1] for i in range(n)]
            cand = [i for i in cand if i not in cur]
            for i in cand:
                cur.append(i)
                dfs(n, cur, maxval)
                cur.pop()

        path = [0]

        dfs(n, path, maxval)
        return self.res


sol = Solution()
print(sol.grayCode(5))
