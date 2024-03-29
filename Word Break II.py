class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """

    def wordBreak(self, s, wordDict):
        return self.dfs(s, wordDict, {})

    # 找到 s 的所有切割方案并 return
    def dfs(self, s, wordDict, memo):
        if s in memo:
            return memo[s]

        if len(s) == 0:
            return []

        partitions = []

        for i in range(1, len(s)):
            prefix = s[:i]
            if prefix not in wordDict:
                continue

            sub_partitions = self.dfs(s[i:], wordDict, memo)
            for partition in sub_partitions:
                partitions.append(prefix + " " + partition)

        if s in wordDict:
            partitions.append(s)

        memo[s] = partitions
        return partitions


sol = Solution()
# print(sol.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
print(sol.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
