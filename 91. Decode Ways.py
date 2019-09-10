class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        if s[1] == 0:
            return 0
        dp[1] = 1
        for i in range(1, len(s) + 1):

            dp[i] += dp[i - 1]
            if i > 1 and int(s[i - 2: i]) <= 26:
                dp[i] += dp[i - 2]
        print(dp)
        return dp[-1]

sol = Solution()
sol.numDecodings("1")