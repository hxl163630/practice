from heapq import *
class Solution:

    def __init__(self):
        self.city = {}


    def inputFlight(self, f):
        n1, n2, d = f.split(":")
        if n1 not in self.city:
            self.city[n1] = [(int(d), n2)]
        else:
            self.city[n1].append((int(d), n2))

        if n2 not in self.city:
            self.city[n2] = [(int(d), n1)]
        else:
            self.city[n2].append((int(d), n1))

        return self.outputDistance()



    def outputDistance(self):
        maxD = 0
        c1 = c2 = c3 = None
        for city, flight in self.city.items():
            if len(flight) < 2: continue
            f = nlargest(2, flight)
            distance = f[0][0] + f[1][0]
            if distance > maxD:
                maxD = distance
                c1 = f[0][1]
                c2 = city
                c3 = f[1][1]
        if not c1: return
        return ":".join([str(maxD), c1,c2,c3])






sol = Solution()
print(sol.inputFlight("CHI:NYC:719"))
print(sol.inputFlight("LA:NYC:2414"))
print(sol.inputFlight("SEATTLE:NYC:2448"))
print(sol.inputFlight("HAWAII:NYC:4924"))

