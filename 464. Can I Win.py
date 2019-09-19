class Solution:
    def canIWin(self, maxInt: int, total: int) -> bool:
        if (maxInt + 1) * maxInt / 2 < total:
            return False
        if total <= 0:
            return True
        memo = {}
        visited = [False for _ in range(maxInt)]
        return self.helper(memo, total, visited)

    def helper(self, memo, total, visited):
        if str(visited) in memo:
            return memo[str(visited)]
        for i, v in enumerate(visited):
            if not v:
                visited[i] = True
                if not self.helper(memo, total - i - 1, visited):
                    memo[str(visited)] = True
                    visited[i] = False
                    return True
                visited[i] = False
        memo[str(visited)] = False
        return False

sol = Solution()
sol.canIWin(10, 11)