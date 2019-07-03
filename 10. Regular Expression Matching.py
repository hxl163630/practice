table = [[False] * (len("sd") ) for _ in range(len("sdf") )]
dp = [[False] * len("sd")] * len("sdf")
table[1][0] = True
dp[1][0] = True
print(table)
print(dp)