# https://leetcode.com/problems/last-stone-weight-ii/discuss/294888/JavaC%2B%2BPython-Easy-Knapsacks-DP
# https://leetcode.com/problems/last-stone-weight-ii/discuss/294881/Another-kind-of-coin-change-problem
class Solution:
    def lastStoneWeightII(self, stones):
        total = sum(stones)
        dp = [False] * (total + 1)
        dp[0] = True
        for s in stones:
            for curSum in range(total, s - 1, -1):
                dp[curSum] |= dp[curSum - s]
        res = total
        for s in range(total):
            if dp[s]:
                res = min(res, abs(total - 2 * s))
        return res
# similar to all subset sum question
