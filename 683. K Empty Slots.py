class Solution:
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        n = len(flowers)
        days = [0] * n
        for i in range(n):
            days[flowers[i] - 1] = i + 1

        left = 0
        right = k + 1
        i = 1
        output = float("inf")
        while right < n:
            if days[i] > days[left] and days[i] > days[right]:
                i += 1
                continue

            if i == right:
                output = min(output, max(days[left], days[right]))

            left = i
            right = i + k + 1
            i += 1
        return output

sol = Solution()
sol.kEmptySlots([1,3,2]
,1)