
class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        output = []

        def dfs(s, index, path, output):
            if index == 4:
                if not s:
                    output.append(path[:-1])
                return  # backtracking
            for i in range(1, 4):
                # the digits we choose should no more than the length of s
                if i <= len(s):
                    # choose one digit
                    if i == 1:
                        dfs(s[i:], index + 1, path + s[:i] + ".", output)
                    # choose two digits, the first one should not be "0"
                    elif i == 2 and s[0] != "0":
                        dfs(s[i:], index + 1, path + s[:i] + ".", output)
                    # choose three digits, the first one should not be "0", and should less than 256
                    elif i == 3 and s[0] != "0" and int(s[:3]) <= 255:
                        dfs(s[i:], index + 1, path + s[:i] + ".", output)
        dfs(s,0,"",output)

        return output

sol = Solution()
print(sol.restoreIpAddresses("172162541"))
