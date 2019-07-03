# graph is in adjacent list representation
graph = {
        'hit': ['hot'],# cog
        'hot': ['hit', 'dot', 'lot'],
        'dot': ['hot', 'dog', 'lot'],
        'dog': ['dot', 'log', 'cog'],
        'lot': ['hot', 'dot'],
        'log': ['lot', 'dog', 'cog'],
        }

def bfs(graph, start, end):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    res = []
    seen = set()
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]

        # path found
        if node == end:
            res.append(path)
            continue
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            if adjacent in path:
                continue
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)
    return res

print(bfs(graph, 'hit', 'cog'))