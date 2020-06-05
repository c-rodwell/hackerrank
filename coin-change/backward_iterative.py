#direct forward method: compute the whole table of sub-problems up to the requested problem.
#iterate from base cases back to the begining.
#problem space: ni = 0 to n, mi = 0 to m (index in c, where m is empty list base case)

def getWays(n,c):
	m = len(c)
	totals = [[None for x in range(n+1)] for y in range(m+1)] # m+1 by n array
	#print(totals)
	#representation: totals[mi][ni] stores ways(ni, c[mi:end]

	#initalize with 0 along mi = m edge since ways(n,[]) = 0
	totals[m] = [0 for x in range(n+1)]

	#initialize with 1 along ni = 0 edge since ways(0,c) = 1
	for y in range(m+1):
		totals[y][0] = 1
	
	#print(totals)
	#iterate over non-initalized part
	for mi in range(m-1, -1, -1):#mi from m-1 to 0, backward:
		coin = c[mi]
		for ni in range(1,n+1):#ni from 1 to n:
			if coin <= ni:	#can use that coin
				totals[mi][ni] = totals[mi][ni - coin] + totals[mi+1][ni]
			else:
				totals[mi][ni] = totals[mi+1][ni]

		#altertnative structure to reduce condition checks:
		# for ni from 1 to coin-1:
		# 	totals[mi, ni] = totals[mi+1,ni]
		# for ni from coin to n:
		# 	totals[mi, ni] = totals[mi, ni - coin] + totals[mi+1,ni]
	#print(totals)
	return totals[0][n]