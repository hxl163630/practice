import math
import numpy as np
#p = [30,35,15,5,10,20,25]
p = [5,10,3,12,5,50,6]
n = len(p) - 1
m = np.zeros((n,n))
km = np.zeros((n,n))


for l in range(2,n+1 + 1):
	for i in range(1, n +1  - l +1):
		j = i +l -1
		print(str(i)+" "+ str(j)+ " "+ str(l))
		m[i-1,j-1] = math.inf
		tmpK = 0
		for k in range(i,j):
			q = m[i-1,k-1] + m[k,j-1]+ p[i-1]* p[k] *p[j]
			if q < m[i-1,j-1]:
				m[i-1,j-1] = q
				tmpK = k
		km[i-1,j-1] = tmpK

print(m)
print(km)
