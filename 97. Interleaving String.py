class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        i = j = 0
        for char in s3:
            if i < len(s1) and s1[i] == char:
                i+=1
                continue
            if j < len(s2) and s2[j] == char:
                j+=1
                continue
            return False
        return True

sol = Solution()
print(sol.isInterleave("aabcc",
"dbbca",
"aadbbcbcac"))