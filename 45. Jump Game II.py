class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        step = curEnd = curReach = 0
        for i in range(len(nums)):
            curReach = max(curReach, nums[i] + i)

            if i == curEnd:
                step += 1
                curEnd = curReach
                if curReach >= len(nums) - 1: break
        return step

        # return dp[0] - 1 if dp[0] > 0 else 0

sol= Solution()
sol.jump([1])