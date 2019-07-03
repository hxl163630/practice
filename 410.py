class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        # divide and conquer -> find the max sum we can get with unknow cut!!
        l = max(nums)
        r = sum(nums)
        while l < r - 1:
            mid = l + (r - l) // 2
            if self.findCutNum(nums, mid) <= m:
                r = mid
            else:
                l = mid

        if self.findCutNum(nums, l) == m:
            return l
        return r

    def findCutNum(self, nums, length):
        res = 1
        leftlength = length
        for num in nums:
            if num <= leftlength:
                leftlength -= num
            else:
                leftlength = length - num
                res += 1
        return res


sol = Solution()
print(sol.splitArray([2,3,1,1,1,1,1],
5))