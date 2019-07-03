class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 < n2:
            return self.findMedianSortedArrays(nums2, nums1)

        minvalue = -float("inf")
        maxvalue = float("inf")
        lo = 0
        hi = n2
        while True:
            mid2 = (lo + hi) // 2
            mid1 = (n1 + n2) // 2 - mid2

            l1 = minvalue if mid1 == 0 else nums1[(mid1 - 1)]
            l2 = minvalue if mid2 == 0 else nums2[(mid2 - 1)]
            r1 = maxvalue if mid1 == n1 else nums1[mid1]
            r2 = maxvalue if mid2 == n2 else nums2[mid2]

            if l1 > r2:
                lo = mid2 + 1
            elif l2 > r1:
                hi = mid2 - 1
            else:
                if 2 * (mid1 + mid2) < (n1 + n2):
                    return min(r1, r2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0


sol = Solution()
print(sol.findMedianSortedArrays([3,4], [1,2]))