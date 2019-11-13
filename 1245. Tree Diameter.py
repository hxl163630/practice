from typing import List
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        from collections import defaultdict
        graph = defaultdict(set)
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
        from heapq import heappushpop, heappush

        self.res = 0

        def helper(cur, graph):
            if len(graph[cur]) == 1:
                return 1

            heap = []
            for neib in graph[cur]:
                if len(heap) == 2:
                    heappushpop(heap, helper(neib, graph))
                else:
                    heappush(heap, helper(neib, graph))
            self.res = max(self.res, sum(heap) + 1)
            return heap[1] + 1

        helper(0, graph)
        return self.res - 1

sol = Solution()
print(sol.treeDiameter([[0,1],[1,2],[2,3],[1,4],[4,5]]))