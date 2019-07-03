class Solution:
    def canJump(self, nums):
        self.res = False

        def dfs(nums, index):
            print(index)
            if index == len(nums) - 1:
                self.res = True
                return
            if nums[index] <= 0:
                return
            nums[index] = -nums[index]

            for i in reversed(range(nums[index], -nums[index] + 1)):
                if 0 <= i + index < len(nums):
                    dfs(nums, i + index)
            nums[index] = -nums[index]

        dfs(nums, 0)
        return self.res

sol = Solution()
print(sol.canJump([8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]))