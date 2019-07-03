class Solution:
    def numTrees(self, n: int) -> int:
        def helper(n, seen):
            if n in seen:
                return seen[n]
            res = 0
            for l in range(n):
                r = n - 1 - l
                left = helper(l, seen)
                right = helper(r, seen)
                if left and right:
                    res += left * right
                if left:
                    res += left
                if right:
                    res += right
            seen[n] = res
            return res

        seen = {}
        seen[0] = 0
        seen[1] = 1

        return helper(n, seen)


sol = Solution()
sol.numTrees(3)