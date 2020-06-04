#recursive with lru cache
import functools

#arguments must be hashable for lru_cache, list is not hashable
#so, convert it to a tuple which is hashable

def getWays(n,c):
	return getWays_lru(n, tuple(c))

@functools.lru_cache
def getWays_lru(n, c):
	if n < 0 : return 0
	if n == 0: return 1
	if len(c) == 0: return 0
	return getWays(n-c[0], c) + getWays(n, c[1:])