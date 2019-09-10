import collections
import bisect
class Solution:
    def makeArrayIncreasing(self, arr1, arr2):
        dp = {-1:0}
        arr2.sort()
        for i in arr1:
            tmp = collections.defaultdict(lambda: float('inf'))
            for key in dp:
                if i > key:
                    tmp[i] = min(tmp[i],dp[key])
                loc = bisect.bisect_right(arr2,key)
                if loc < len(arr2):
                    tmp[arr2[loc]] = min(tmp[arr2[loc]],dp[key]+1)
            dp = tmp
        if dp:
            return min(dp.values())
        return -1

if __name__ == "__main__":
    sol = Solution()
    sol.makeArrayIncreasing([1,5,3,6,7], [1,3,2,4])