def maxSumTwoNoOverlap(A, L, M):
    B = A[:]
    for i in range(1, len(A)):
        B[i] += B[i - 1]
    res, Lmax, Mmax = B[L + M - 1], B[L - 1], B[M - 1]
    for i in range(L + M, len(B)):
        Lmax = max(Lmax, B[i - M] - B[i - L - M])
        Mmax = max(Mmax, B[i - L] - B[i - L - M])
        res = max(res, Lmax + B[i] - B[i - M], Mmax + B[i] - B[i - L])
    return res

maxSumTwoNoOverlap([0,6,5,2,2,5,1,9,4], 1, 2)