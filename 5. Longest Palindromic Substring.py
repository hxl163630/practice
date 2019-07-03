class Solution(object):
    def longestPalindromeDP(self, s):##DP solution time:o(n2) space: o(1)
        """
        :type s: str
        :rtype: str
        """
        longest = s[0]
        for i in range(len(s)):
            s_odd = self.findbyindexDP(s, i, i)
            s_even = self.findbyindexDP(s, i, i + 1)
            if len(s_odd) > len(longest): longest = s_odd
            if len(s_even) > len(longest): longest = s_even
        return longest

    def findbyindexDP(self, s, i, j):
        if j >= len(s): return ""
        while (s[i] == s[j]):
            i -= 1
            j += 1
            if (i < 0 or j >= len(s)): break
        return s[i + 1: j]


    def longestPalindromeManacher(self,s):
        L = R = c = 0
        T = '#'.join('^{}$'.format(s))
        P = [0] * len(T)
        for i in range(1,len(T)-1):
            i_mirror = 2 *c - i
            P[i] = (R > i) and min(R - i, P[i_mirror]);

            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            if i + P[i] > R:
                c,R  = i , i+P[i]

        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))

        return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]



    def findbyindexManacher(self, s, i):
        ip = i
        while (s[i] == s[ip]):
            i += 1
            ip -= 1
            if(i<0 or ip>=len(s)): break
        return i, ip


s = Solution()
#print(s.longestPalindromeDP("ababad"))
print(s.longestPalindromeManacher("ababad"))