class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        output = 0
        for i, d1 in enumerate(num1[::-1]):
            tmp = 0
            for j, d2 in enumerate(num2[::-1]):
                tmp += int(d2) * int(d1) * 10 ** i * 10 ** j
            output += tmp
        return str(output)

sol = Solution()
sol.multiply("123","456")