class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if not A: return None
        output = []
        for curSize in range(len(A) - 1, 0, -1):
            maxi = A.index(max(A[:curSize]))
            if maxi != curSize:
                tmp = A[:maxi + 1]
                A[:maxi+ 1] = tmp[::-1]
                tmp = A[:curSize + 1]
                A[:curSize+1] = tmp[::-1]
                output+=[maxi + 1, curSize + 1]
        return output

sol = Solution()
print(sol.pancakeSort([3,2,4,1]))