from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict)
        minLen = min(len(a) for a in wordDict)

        def helper(s, wordset, index, minlen):
            for i in range(index + minlen, len(s) + 1 - minlen):
                if s[index:i] in wordset and s[i:] in wordset or helper(s, wordset, i, minlen):
                    return True
            return False


        return helper(s, wordset, 0, minLen)


sol = Solution()
print(sol.wordBreak("a", ["a"]))