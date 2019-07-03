class Solution:
    def isMatch(self, s: 'str', p: 'str') -> 'bool':
        si = pi = match = 0
        starIdx = -1
        while si < len(s):
            if pi < len(p) and (p[pi] == "?" or p[pi] == s[si]):
                si += 1
                pi += 1
            elif pi < len(p) and p[pi] =="*":
                starIdx = pi
                match = si
                pi += 1
            elif starIdx != -1:
                pi = starIdx + 1
                match += 1
                si = match
            else: return False
        while pi < len(p) and p[pi] == "*":
            pi += 1
        return pi == len(p)

sol = Solution()
sol.isMatch(s = "adcebb" ,p = "*a*b")