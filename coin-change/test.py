import random
import time
import recursive
import recursive_lru
import memoized

methods = [
	("simple recursive", recursive.getWays),
	("lru cache recursive", recursive_lru.getWays),
	("wrapper memoized", memoized.getWays)]

def compareAll(n, c):
	print("comparison for n = "+str(n)+", c = "+str(c))
	for name, method in methods:
		print("\n"+name+":")
		before = time.time()
		answer = method(4, [1,2,3])
		elapsed = time.time() - before
		print("answer = "+str(answer))
		print("elapsed = "+str(elapsed))

#basic test is: getWays(4, [1,2,3]) = 4
def basicTest():
	compareAll(4, [1,2,3])

MAX_C = 50
MAX_N = 250
MAX_M = 50

def shuffleTest(m,n):
	return