class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        def ispalindrome(s, start, end):
            while start < end:
                if s[start] == s[end]:
                    start += 1
                    end -= 1
                else: return False
            return True

        res = []

        def dfs(s, start, cur, res):
            if start == len(s):
                res.append(cur[:])
                return
            for i in range(start, len(s)):
                if ispalindrome(s, start, i):
                    cur.append(s[start: i + 1])
                    dfs(s, i + 1, cur, res)
                    cur.pop()

        dfs(s, 0, [], res)
        return res
sol = Solution()
sol.partition("aab")