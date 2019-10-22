a = [15, 5, 15, 20, 30]

def findmintime(a):
    l = 0
    r = sum(a)
    while l < r - 1:
        m = (l + r) // 2
        if count(a, m):
            r = m
        else:
            l = m

    if count(a, l):
        return l
    return r
def count(a, m):
    cur = [m, m, m]
    for i in a:
        if i > m or max(cur) < i:
            return False
        index = cur.index(max(cur))
        cur[index] -= i
    return True



print(findmintime(a))