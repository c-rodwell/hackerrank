#like memoized_index, but pass c as global.

def getWays(n,c):
	memo = {}
	i = len(c) - 1
	global c2
	c2 = c
	return ways_inner(n, i, memo)

def ways_inner(n, i, memo):
	if (n,i) in memo:
		return memo[(n,i)]
	elif n < 0 :
		retval = 0
	elif n == 0:
		retval = 1
	elif i < 0:
		retval = 0
	else:
		retval = ways_inner(n-c2[i], i, memo) + ways_inner(n, i-1, memo)
	memo[(n,i)] = retval
	return retval