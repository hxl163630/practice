#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    dic = {}
    for i in s:
        i = i % k
        dic[i] = dic.get(i, 0) + 1
    keys = list(dic.keys())
    n = len(keys)
    res = 0
    for i in range(n):
        for j in range(i, n):
            if (keys[i] + keys[j]) % k != 0:
                if i == j:
                    res += dic[keys[i]] * (dic[keys[i]] - 1) // 2
                else:
                    res += dic[keys[i]] * dic[keys[j]]
    return res


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)
    print(result)
