class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # dp[i] = min[dp[i-k] + 1 for k in coins if dp[i-k] >= 0]

        MAX = float('inf')
        dp = [0] + [MAX] * amount

        for i in range(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1
        tmp1 = [dp[amount], -1]
        tmp2 = [dp[amount] == MAX]
        return [dp[amount], -1][dp[amount] == MAX]


sol = Solution()
print(sol.coinChange([1, 2, 5], 11))