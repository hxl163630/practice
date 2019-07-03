class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s: return ""
        if numRows == 1: return s
        outputList = []
        for i in range(numRows):
            outputList.append([])
        loopNum = (numRows - 1) * 2
        for i in range(len(s)):
            if i % loopNum < numRows:
                outputList[i % loopNum].append(s[i])
            else:  # i = 4 loopnum = 6
                outputList[-((i - numRows + 2) % loopNum)].append(s[i])
        output = ""
        if len(s) >= numRows:
            for i in outputList:
                for j in i:
                    output += j

        else:
            for i in outputList:
                if i:
                    output += i[0]
        return output

sol = Solution()
print(sol.convert("A",2))