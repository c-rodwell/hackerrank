#simple recursive version:

def getWays(n, c):
	if n < 0 : return 0
	if n == 0: return 1
	if len(c) == 0: return 0
	return getWays(n-c[0], c) + getWays(n, c[1:])