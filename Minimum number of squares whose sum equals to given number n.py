# A dynamic programming based Python
# program to find minimum number of
# squares whose sum is equal to a
# given number

# Returns count of minimum squares
# that sum to n
def getMinSquares(n):
    # Create a dynamic programming table
    # to store sq and getMinSquares table
    # for base case entries
    dp = [0, 1, 2, 3]
    p = [[],[1],[1,1],[1,1,1]] # output of xi list
    # getMinSquares rest of the table
    # using recursive formula
    for i in range(4, n + 1):

        # max value is i as i can always
        # be represented as 1*1 + 1*1 + ...
        dp.append(i)
        tmpx = 0 # use to store the last time that dp[i] changes
        # Go through all smaller numbers
        # to recursively find minimum
        for x in range(1, i + 1):
            temp = x * x;
            if temp > i:
                break
            else:
                if(dp[i] > 1 + dp[i- temp]):
                    tmpx = x # use to store the last time that dp[i] changes
                dp[i] = min(dp[i], 1 + dp[i - temp])

        tmp = p[i - tmpx * tmpx]+ [tmpx]
        p.append(tmp)
            # Store result
    return dp[n], p[n]


# Driver program
for i in range(1,1001):
    tmp = getMinSquares(i)
    print(str(i) + " "+ str(tmp[0])+ " "+ str(tmp[1]) + " "+ str(sum(x * x for x in tmp[1])))

# This code is contributed by nuclode
