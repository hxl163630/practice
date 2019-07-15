class Solution:
    def fullJustify(self, words, maxWidth: int):

        def getSpaces(cur, maxWidth):
            spaceSlot = len(cur) - 1
            totalSpace = maxWidth - sum(len(i) for i in cur)
            count = totalSpace // spaceSlot
            remain = totalSpace % spaceSlot
            res = []
            for i in range(spaceSlot):
                if i < remain:
                    res.append(count + 1)
                else:
                    res.append(count)
            res.append(0)
            return res

        curlength = maxWidth
        cur = []
        res = []

        for word in words:
            if curlength >= len(word):
                cur.append(word)
                curlength -= len(word) + 1
            else:
                if len(cur) == 1:
                    res.append(cur[0] + " " * (maxWidth - len(cur[0])))
                else:
                    spaces = getSpaces(cur, maxWidth)
                    tmp = []
                    for w, space in zip(cur, spaces):
                        tmp.append(w)
                        tmp.append(" " * space)
                    res.append("".join(tmp))

                cur = [word]
                curlength = maxWidth - len(word) - 1

        last = " ".join(cur)
        res.append(last + " " * (maxWidth - len(last)))
        return res

sol = Solution()
sol.fullJustify(["a","computer.","Art","is","everything","else","we","do"],
20)