class Solution:
    def rotatedDigits(self, N: int) -> int:

        dp = [[False, False] for _ in range(N + 1)]
        dic = {"1": "1", "2": "5", "5": "2", "8": "8", "0": "0", "6": "9", "9": "6"}
        dp[0][0] = True
        for i in range(N + 1):
            if i <= 9:
                if i == 1 or i == 8:
                    dp[i][0] = True
                if i == 2 or i == 5 or i == 6 or i == 9:
                    dp[i][0] = dp[i][1] = True
                continue
            s = str(i)
            first = s[0]
            last = s[-1]
            mid = s[1: -1]
            if mid == "":
                mid = 0
            else:
                mid = int(mid)
            if first in dic and dic[first] == last:
                dp[i][0] = dp[mid][0]
                if first in "180":
                    dp[i][1] = dp[mid][1]
                else:
                    dp[i][1] = True

sol = Solution()
sol.rotatedDigits(100)