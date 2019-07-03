class Solution:
    def findTargetSumWays(self, nums, S: int) -> int:
        total = sum(nums)
        if S > total or S < -total: return 0
        dp = [[0] * (total * 2 + 1) for _ in range(2)]
        dp[0][total] = 1
        for i, num in enumerate(nums):
            dp[(i + 1) % 2] = [0] * (total * 2 + 1)
            for k in range(2 * total + 1):
                if dp[i % 2][k] != 0:
                    dp[(i + 1) % 2][k + num] += dp[i % 2][k]
                    dp[(i + 1) % 2][k - num] += dp[i % 2][k]

        return dp[(len(nums) - 1) % 2][total]

sol = Solution()
sol.findTargetSumWays([1,1,1,1,1],3)

