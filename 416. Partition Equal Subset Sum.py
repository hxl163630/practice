class Solution:
    def canPartition(self, nums) -> bool:
        total = sum(nums)
        if total & 1 == 1:
            return False
        target = total >> 1
        n = len(nums)
        # dp[i][j] whether the first i nums can form sum j
        dp = [[False for _ in range(target + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            for j in range(target + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = False
                elif j == 0:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i - 1][j]
                    if j - nums[i - 1] >= 0:
                        dp[i][j] |= dp[i][j - nums[i - 1]]
        return dp[n][target]