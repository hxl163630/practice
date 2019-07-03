class TrieNode:
    def __init__(self):
        self.index = -1
        self.sons = {}
        self.indexlist = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def ispalindrome(self, word, l, r):
        while l < r:
            if word[l] != word[r]:
                return False
            l += 1
            r -= 1
        return True

    def insert(self, word, index):
        node = self.root

        for i in range(len(word) - 1, -1, -1):
            c = word[i]
            if c not in node.sons:
                node.sons[c] = TrieNode()
            if self.ispalindrome(word, 0, i):
                node.indexlist.append(index)
            node = node.sons[c]
        node.index = index
        node.indexlist.append(index)

    def searchPair(self, res, word, index1):
        node = self.root
        for i, c in enumerate(word):
            if node.index >= 0 and node.index != index1 and self.ispalindrome(word, i, len(word) - 1):
                res.append([index1, node.index])
            if c not in node.sons:
                return
            node = node.sons[c]

        for index2 in node.indexlist:
            if index1 == index2:
                continue
            res.append([index1, index2])
        return res


class Solution:
    def palindromePairs(self, words):
        trie = Trie()
        for i, w in enumerate(words):
            trie.insert(w, i)
        res = []
        for i, w in enumerate(words):
            trie.searchPair(res, w, i)
        return res


sol = Solution()
sol.palindromePairs(["ba", "a", "aaa"])