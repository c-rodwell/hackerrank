#make lru version use index - then don't need to pass tuple
#but then we stil need to have c accsessible - make a constant or something?
#as in memoized_index: i goes from len(c)-1 down to -1

#this seems to work correctly without clearing cache, even though cached (n,i) would seem to interfere with same (n,i) for different c
	#maybe lru_cache defined inside the function only exists within the function.

import functools

def getWays(n,c):

	@functools.lru_cache
	def getWays_lru(n, i):
		if n < 0 : return 0
		if n == 0: return 1
		if i < 0: return 0
		return getWays_lru(n-c[i], i) + getWays_lru(n, i-1)

	return getWays_lru(n, len(c) -1)

