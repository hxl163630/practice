class Solution:
    def wordPatternMatch(self, pattern: 'str', str: 'str') -> 'bool':
        dic = {char: "" for char in set(pattern)}

        def dfs(t, p, dic):  # t: target, p: pattern
            if not len(p) and not len(p): return True
            if not len(p) and len(t): return False
            curP = dic[p[0]]
            if curP != "":
                if t.startswith(curP):
                    return dfs(t[len(curP):], p[1:], dic)
                return False

            else:
                for i in range(len(t)):
                    dic[p[0]] = t[: i + 1]
                    res = dfs(t[i + 1:], p[1:], dic)
                    if res: return True
                    dic[p[0]] = ""
                return False

        res = dfs(str, pattern, dic)
        if len(dic) != len(set(dic.values())): return False
        return res

        return dfs(str, pattern, dic)









sol = Solution()
print(sol.wordPatternMatch("edcs",
"electronicengineeringcomputerscience"))
