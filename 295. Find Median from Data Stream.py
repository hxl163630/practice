import heapq


class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """

    def medianII(self, nums):
        if not nums:
            return []

        self.median = nums[0]
        self.maxheap = []
        self.minheap = []

        medians = [nums[0]]
        for num in nums[1:]:
            self.add(num)
            medians.append(self.median)

        return medians

    def add(self, num):
        if num < self.median:
            heapq.heappush(self.maxheap, -num)
        else:
            heapq.heappush(self.minheap, num)

        # balanace
        if len(self.maxheap) > len(self.minheap):
            heapq.heappush(self.minheap, self.median)
            self.median = -heapq.heappop(self.maxheap)
        elif len(self.maxheap) + 1 < len(self.minheap):
            heapq.heappush(self.maxheap, -self.median)
            self.median = heapq.heappop(self.minheap)

sol = Solution()
print(sol.medianII([4,2,5,6,7,5,6,2,12,564,43,4352]))