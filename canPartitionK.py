import copy
class Solution:
    def canPartitionKSubsets(self, nums, k):
        self.min_time = float('inf')
        self.ans = []
        self.dfs(nums, [[] for _ in range(k)], 0, k)
        return self.ans

    def dfs(self, nums, workers, idx, k):
        if idx >= len(nums):
            min_time = max(sum(worker) for worker in workers)
            if min_time < self.min_time:
                self.min_time = min_time
                self.ans = copy.deepcopy(workers)
            return
        for i in range(k):
            workers.append(nums[idx])
            self.dfs(nums, workers, idx + 1, k)
            workers.pop()


nums = [15,5,15,20,30]
k = 3
s = Solution()
print(s.canPartitionKSubsets(nums, k))