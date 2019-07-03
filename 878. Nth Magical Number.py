class Solution(object):
    def gcd(self, x, y):
        while y > 0:
            x, y = y, x % y
        return x

    def lcm(self, x, y):
        return x * y // self.gcd(x, y)

    def nthMagicalNumber(self, N, A, B):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """

        lcm1 = self.lcm(A, B)
        i = min(A, B)
        candidate = []
        while i <= lcm1:
            if i % A == 0 or i % B == 0:
                candidate.append(i)
            i += 1
        output = ((N-1)//len(candidate))*candidate[-1] + candidate[N%len(candidate)-1]
        return output

sol = Solution()
sol.nthMagicalNumber(5,4,2)