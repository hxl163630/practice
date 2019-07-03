class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """

    def rerange(self, A):
        if not A or len(A) == 1:
            return

        posCount = 0
        posIndex = 1
        negIndex = 0
        n = len(A)

        if n % 2:
            for num in A:
                if num > 0:
                    posCount += 1

            if posCount >= (n // 2):
                posIndex = 0
                negIndex = 1

        while posIndex < n and negIndex < n:
            while posIndex < n and A[posIndex] > 0:
                posIndex += 2
            while negIndex < n and A[negIndex] < 0:
                negIndex += 2
            if posIndex < n and negIndex < n:
                A[posIndex], A[negIndex] = A[negIndex], A[posIndex]
sol = Solution()
sol.rerange([-13,-8,-12,-15,-14,35,7,-1,11,27,10,-7,-12,28,18])