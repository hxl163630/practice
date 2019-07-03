class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace("-", "").upper()
        output = ""

        offset = len(S) % K
        for i in range(len(S) // K + 1):
            if K * (i - 1) + offset < 0:
                output += S[0: K * (i) + offset] + "-"
            else:
                output += S[K * (i - 1) + offset: K * (i) + offset] + "-"
        return output[:-1]

sol = Solution()
sol.licenseKeyFormatting("5F3Z-2e-9-w", 4)