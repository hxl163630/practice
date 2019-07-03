class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle: return 0
        if not haystack: return -1
        n = len(haystack)
        m = len(needle)
        if m > n: return -1

        mod = 100000
        hashc = 31

        power = 1  # hashc ** m
        code = 0
        target = 0

        for i in range(m):
            power = (power * hashc) % mod

        for i in range(m):
            target = (target * hashc + ord(needle[i])) % mod

        for i in range(n):
            code = (code * hashc + ord(haystack[i])) % mod

            if i >= m:
                code = code - (power * ord(haystack[i - m])) % mod
                if code < 0: code += mod

            if haystack[i - m:i] == needle: return i - m

        return -1

sol = Solution()
sol.strStr("a","a")