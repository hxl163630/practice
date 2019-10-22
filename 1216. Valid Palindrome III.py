from functools import lru_cache

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    dp[i][j] = i + j
                elif s[i - 1] == s[n - j]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
        return dp[n][n] <= k * 2

    def isValidPalindrome1(self, s: str, k: int) -> bool:
        @lru_cache(maxsize=None)
        def dfs(s, l, r):
            if l >= r:
                return 0
            if s[l] == s[r]:
                return dfs(s, l + 1, r - 1)
            return min(dfs(s, l + 1, r), dfs(s, l, r - 1)) + 1

        return dfs(s, 0, len(s) - 1) <= k

    def isValidPalindrome2(self, s: str, k: int) -> bool:
        def dfs(s, l, r, seen):
            if l >= r:
                return 0
            if (l, r) in seen:
                return seen[(l, r)]
            if s[l] == s[r]:
                res = dfs(s, l + 1, r - 1, seen)
            else:
                res = min(dfs(s, l + 1, r, seen), dfs(s, l, r - 1, seen)) + 1
            seen[(l, r)] = res
            return res
        seen = {}
        return dfs(s, 0, len(s) - 1, seen) <= k

sol = Solution()
a = "asdfasdfasasdfaasdfasdfasdfaasasdfasdfasdfaasdfasdfasdfaafasdfasdfaaasdfasdfasdfaasdfasdfasdfaasdfasdfasdfaasdfasdfasdfaasdfasdfasdfaasdfasdfasdfaasdfasdfasdfaasdfasdfasdfaasdfasdfasdfaasdfasdfasdfa"
k = 50
print(len(a))

import time

t1 = time.time()
print(sol.isValidPalindrome(a, k))
t2 = time.time()
print(sol.isValidPalindrome1(a, k))
t3 = time.time()



print(sol.isValidPalindrome2(a, k))
t4 = time.time()
print(t2 - t1, t3 - t2, t4 - t3)