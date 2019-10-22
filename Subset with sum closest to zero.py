# Python3 Code for above implementation
# https://www.geeksforgeeks.org/subset-with-sum-closest-to-zero/
import numpy as np

arrSize = 51
maxSum = 201
MAX = 100
inf = 999999

# Variable to store states of dp
dp = np.zeros((arrSize, maxSum))
visit = np.zeros((arrSize, maxSum))
k = -11

# Function to return the number closer to integer s
def RetClose(a, b, s):
    if (abs(a - s) < abs(b - s)):
        return a
    else:
        return b

    # To find the sum closest to zero


# Since sum can be negative, we will add MAX
# to it to make it positive
def MinDiff(i, sum, arr, n):
    # Base cases
    if (i == n):
        return 0

        # Checks if a state is already solved
    if (visit[i][sum + MAX]):
        return dp[i][sum + MAX]

    visit[i][sum + MAX] = 1

    # Recurrence relation
    dp[i][sum + MAX] = RetClose(arr[i] + MinDiff(i + 1, sum + arr[i], arr, n),
                                MinDiff(i + 1, sum, arr, n),
                                -1 * sum + k)

    # Returning the value
    return int(dp[i][sum + MAX])


# Function to calculate the closest sum value
def FindClose(arr, n):
    ans = inf

    # Calculate the Closest value for every
    # subarray arr[i-1:n]
    for i in range(1, n + 1):
        ans = RetClose(arr[i - 1] + MinDiff(i, arr[i - 1], arr, n), ans, k)

    print(ans)


# Driver function
if __name__ == "__main__":
    # Input array
    arr = [25, -9, -10, -4, -7, -33]
    n = len(arr)

    FindClose(arr, n)

    # This code is contributed by AnkitRai01