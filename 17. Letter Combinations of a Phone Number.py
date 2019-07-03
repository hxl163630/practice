class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        i = 0
        output = []
        while i < len(digits):
            if output == []:
                output = list(dic[digits[i]])
                i += 1
                continue
            tmp = [0]
            for j in range(len(digits[i])):
                tmp = [ x + dic[digits[j]] for x in output]
            output = tmp[1:]
            i += 1
        return output
sol = Solution()
sol.letterCombinations("23")