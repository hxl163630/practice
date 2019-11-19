from typing import List
class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        from collections import defaultdict
        graph = defaultdict(list)
        for r in regions:
            graph[r[0]] += r[1:]

        def dfs(graph, cur, r1, r2):
            if cur not in graph:
                return ""
            if cur == r1 or cur == r2:
                return cur
            findCount = 0
            res = ""
            for nxt in graph[cur]:
                son = dfs(graph, nxt, r1, r2)
                if son != "":
                    findCount += 1
                    res = son
            if findCount == 2:
                return cur
            if findCount == 1:
                return res
            return ""

        for k in graph.keys():
            res = dfs(graph, k, region1, region2)
            if res:
                return res
        return ""

sol = Solution()
print(
sol.findSmallestRegion([["Earth","North America","South America"],["North America","United States","Canada"],["United States","New York","Boston"],["Canada","Ontario","Quebec"],["South America","Brazil"]],
"Quebec",
"New York"))