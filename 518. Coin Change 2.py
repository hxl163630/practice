class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount + 1)
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
        for i in range(1,amount + 1):
            for coin in coins:
                if i >= coin and dp[i-coin] != 0:
                    dp[i] += dp[i-coin] + 1
        return dp[-1]

sol = Solution()
sol.change(5,[1,2,5])