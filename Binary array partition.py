"""
Z is a binary array with 1s and 0s
If it is possible, return any [i, j], such that
* Z[0], Z[1], ..., Z[i] is the first part;
* Z[i+1], Z[i+2], ..., Z[j-1] is the second part, and
* Z[j], Z[j+1], ..., Z[Z.length - 1] is the third part.
* All three parts have equal binary value.
"""

def divide_arr(input):
    ones = 0
    for c in input:
        ones += (c == "1")
    if ones % 3 != 0:
        return (-1, -1)
    target_ones = ones // 3
    leftOnes = 0
    a = 0
    for l in range(len(input)):
        leftOnes += (input[l] == "1")
        a <<= 1
        a += (input[l] == "1")
        if leftOnes < target_ones:
            continue
        if leftOnes > target_ones:
            return (-1, -1)
        # a = int(input[:l + 1], 2)
        midOnes = 0
        b = 0
        for m in range(l + 1, len(input)):
            midOnes += (input[m] == "1")
            b <<= 1
            b += (input[m] == "1")
            if midOnes < target_ones:
                continue
            if midOnes > target_ones:
                break
            # b = int(input[l + 1: m + 1], 2)

            c = int(input[m + 1:], 2)
            if a == b == c:
                return (l, m + 1)



    return (-1, -1)


import time
input = ("0" * 10000000 + "1") * 3
t1 = time.time()
print(divide_arr(input))
t2 = time.time()
print(t2 - t1)

