#lru with index on c, pass c with global keyword
#as in memoized_index: i goes from len(c)-1 down to -1
#need to clear cache since lru cache only stores (n,i) - otherwise it will give wrong answer calling with different c

import functools

def getWays(n,c):
	global c2
	c2 = c
	getWays_lru.cache_clear() 
	return getWays_lru(n, len(c) -1)

@functools.lru_cache
def getWays_lru(n, i):
	if n < 0 : return 0
	if n == 0: return 1
	if i < 0: return 0
	return getWays_lru(n-c2[i], i) + getWays_lru(n, i-1)