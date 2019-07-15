class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        chars = sorted(list(tiles))
        self.res = 0
        def dfs(nums, index):
            if index == len(nums):
                self.res += 1
                return
            for i in range(index, len(nums)):

                dfs(nums, i + 1)
        dfs(chars, 0)
        return self.res

sol = Solution()
sol.numTilePossibilities("AAB")