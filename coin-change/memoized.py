#memoized recursive version

def getWays(n,c):
	memo = {}
	return ways_inner(n, tuple(c), memo)

def ways_inner(n, c, memo):
	if (n,c) in memo:
		return memo[(n,c)]
	elif n < 0 :
		retval = 0
	elif n == 0:
		retval = 1
	elif len(c) == 0:
		retval = 0
	else:
		retval = ways_inner(n-c[0], c, memo) + ways_inner(n, c[1:], memo)
	memo[(n,c)] = retval
	return retval