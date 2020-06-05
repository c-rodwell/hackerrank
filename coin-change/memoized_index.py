#change memoized version to use index in c, so list itself doesn't change.
#sublist is c[i:] - pass i, keep c unchanged
#current coin value is c[i], for i = 0 to len(c)-1
#since order doesn't matter, have i go from len(c)-1 downward, base case at i= -1 (empty list)

def getWays(n,c):
	memo = {}
	i = len(c) - 1
	return ways_inner(n, c, i, memo)

def ways_inner(n, c, i, memo):
	if (n,i) in memo:
		return memo[(n,i)]
	elif n < 0 :
		retval = 0
	elif n == 0:
		retval = 1
	elif i < 0:
		retval = 0
	else:
		retval = ways_inner(n-c[i], c, i, memo) + ways_inner(n, c, i-1, memo)
	memo[(n,i)] = retval
	return retval