class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        dic = Counter(t)
        r = 0
        n = len(s)
        count = len(dic)
        resLen = len(s)
        res = ""
        for l, c in enumerate(s):
            while r < n and count > 0:
                if s[r] in dic:
                    dic[s[r]] -= 1
                    if dic[s[r]] == 0:
                        count -= 1
                r += 1
            if r - l < resLen and count == 0:
                resLen = r - l
                res = s[l: r]
            if c in dic:
                if dic[c] == 0:
                    dic[c] += 1
                    count += 1
        return res

sol = Solution()
print(sol.minWindow("ADOBECODEBANC","ABC"))
