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
                        dp[i][j] |= dp[i - 1][j - nums[i - 1]]
        print(dp[n][target])
        return dp[n][target]

sol = Solution()
sol.canPartition([51,54,10,76,88,53,32,37,61,43,10,26,52,26,21,65,70,94,87,14,48,10,18,6,63,57,69,98,45,36,58,39,90,80,58,16,54,5,88,54,19,38,68,33,38,42,83,28,2,97,7,49,11,67,93,20,90,10,60,19,99,22,61,98,78,21,46,73,17,77,65,81,46,16,12,70,13,19,2,88,83,42,70,73,95,49,61,31,66,50,14,66,73,69,7,18,69,57,12,83])