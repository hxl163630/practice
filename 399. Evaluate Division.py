class Solution:
    def calcEquation(self, equations, values, queries):
        f = {}
        dist = {}

        def find(a):
            if a not in f:
                f[a] = a
                dist[a] = 1
                return a
            if f[a] == a:
                return a
            lastp = f[a]
            p = find(lastp)
            f[a] = p
            dist[a] = dist[a] * dist[lastp]
            return p


        for eq, val in zip(equations, values):
            a, b = eq
            fa = find(a)
            fb = find(b)
            f[fa] = fb
            dist[fa] = dist[b] * val / dist[a]

        res = []
        for q in queries:
            a, b = q
            if a not in f or b not in f or find(a) != find(b):
                res.append(float(-1))
                continue
            res.append(float(dist[a] / dist[b]))
        print(res)
        return



sol = Solution()
sol.calcEquation([["a","b"],["e","f"],["b","e"]],
[3.4,1.4,2.3],
[["b","a"],["a","f"],["f","f"],["e","e"],["c","c"],["a","c"],["f","e"]])
