class Solution:
    def permuteUnique(self, nums):
        def backtrack(cur, nums):
            if len(cur) == len(nums):
                ans.append(cur)
                return

            for i in range(len(nums)):
                if i > 0 and nums[i - 1] == nums[i] and not visited[i - 1]:
                    continue
                if visited[i]:
                    continue
                visited[i] = True
                backtrack(cur + [nums[i]], nums)
                visited[i] = False

        ans = []
        nums.sort()
        visited = [False] * len(nums)
        backtrack([], nums)
        return ans

sol = Solution()
sol.permuteUnique([1,1,2])