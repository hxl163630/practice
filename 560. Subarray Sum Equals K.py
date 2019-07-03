class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = {0: 1}
        res = presum = 0
        for num in nums:
            presum += num
            res += dic.get(presum - k, 0)
            dic[presum] = dic.get(presum, 0) + 1
        return res

sol = Solution()
sol.subarraySum([1,1,1],2)