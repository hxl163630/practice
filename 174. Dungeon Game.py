class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon or not dungeon[0]: return 0
        dp = [[0 for _ in dungeon[0]] for _ in dungeon]
        m = len(dungeon)
        n = len(dungeon[0])
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    dp[i][j] = max(1, 1-dungeon[i][j])
                elif i == m-1:
                    dp[i][j] = max(1, dp[i][j+1] - dungeon[i][j])
                elif j == n-1:
                    dp[i][j] = max(1, dp[i+1][j] - dungeon[i][j])
                else:
                    dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])
        return dp[0][0]

sol = Solution()
print(sol.calculateMinimumHP([[1,-3,3],[0,-2,0],[-3,-3,-3]]))