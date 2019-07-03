import collections
import heapq
def leastInterval(tasks, n):
    """
    :type tasks: List[str]
    :type n: int
    :rtype: int
    """
    n += 1
    ans = 0
    d = collections.Counter(tasks)
    heap = [-c for c in d.values()]
    heapq.heapify(heap)
    while heap:
        stack = []
        cnt = 0
        for _ in range(n):
            if heap:
                c = heapq.heappop(heap)
                cnt += 1
                if c < -1:
                    stack.append(c + 1)
        for item in stack:
            heapq.heappush(heap, item)
        ans += heap and n or cnt  # == if heap then n else cnt
    return ans

tasks = ["A","A","A","B","B"]
n = 2
leastInterval(tasks, n)