import heapq


class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        sortWorker = sorted([float(w / q), q] for w, q in zip(wage, quality))
        output = float("inf")
        qsum = 0
        heap = []
        for r, q in sortWorker:
            heapq.heappush(heap, -q)
            qsum += q
            if len(heap) > K:
                qsum += heapq.heappop(heap)
            if len(heap) == K:
                output = min(output, qsum * r)
        return output


sol = Solution()
sol.mincostToHireWorkers([3,1,10,10,1], [4,8,2,2,7], 3)

