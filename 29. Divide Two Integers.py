class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        output = 0

        sign = 1 if (dividend > 0) == (divisor > 0) else -1
        dividend, divisor = abs(dividend), abs(divisor)
        while dividend >= divisor:
            tmp = divisor
            exp = 0
            while dividend >= tmp << 1:
                tmp <<= 1
                exp += 1
            dividend -= tmp
            output += 1 << exp
        return output * sign

sol = Solution()
print(sol.divide(10,3))