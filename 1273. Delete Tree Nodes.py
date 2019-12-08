from typing import List
class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        from collections import Counter, deque, defaultdict
        pCnt = Counter(parent)
        q = deque([a for a in range(nodes) if a not in pCnt])

        while q:
            cur = q.popleft()
            value[parent[cur]] += value[cur]
            pCnt[parent[cur]] -= 1
            if pCnt[parent[cur]] == 0:
                q.append(parent[cur])
        sons = defaultdict(list)
        for node, parent in enumerate(parent):
            sons[parent].append(node)
        res = 0
        q = deque(sons[-1])
        print(value)
        while q:
            cur = q.popleft()
            if value[cur] == 0:
                continue
            q += sons[cur]
            res += 1
        return res

sol = Solution()
sol.deleteTreeNodes(7,
[-1,0,0,1,2,2,2],
[1,-2,4,0,-2,-1,-1])