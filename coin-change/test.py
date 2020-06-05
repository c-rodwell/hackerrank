import random
import time
import recursive
import lru
import lru_mistake
import lru_index
import lru_index_global
import memoized
import memoized_index
import memoized_index_global
import backward_iterative
import iterative_alt


methods = [
	("memoized on index", memoized_index.getWays),
	("memoized index with global c", memoized_index_global.getWays),
	("memoized on tuple", memoized.getWays),
	("iterative original", backward_iterative.getWays),
	("iterative altered", iterative_alt.getWays),
	("lru index with inner function", lru_index.getWays),
	("lru index with global c", lru_index_global.getWays),
	("lru cache simplest form", lru.getWays),
	("lru cache recursive with mistake", lru_mistake.getWays),
	("simple recursive", recursive.getWays)
	]

def compareAll(n, c):
	print("comparison for n = "+str(n)+", c = "+str(c))
	for name, method in methods:
		print("\n"+name+":")
		before = time.time()
		answer = method(n, c)
		elapsed = time.time() - before
		print("answer = "+str(answer))
		print("elapsed = "+str(elapsed))

#basic test is: getWays(4, [1,2,3]) = 4
def basicTest():
	compareAll(4, [1,2,3])

#required range is 1 <= c[i] <= 50, 1 <= n <= 250, 1 <= m <= 50, all c[i] distinct
#since ci are distinct, at max size 50, c is a permutation of the numbers 1-50
#(or at smaller size, can be some subset of 1-50)
#order shouldn't matter, but shuffle anyway to see that it doesn't affec the answer.
MAX_C = 50
MAX_N = 250
MAX_M = 50

#
def shuffleTest(m,n):
	c = [x for x in range(1, m+1)]
	random.shuffle(c)
	compareAll(n, c)

def maxRequiredTest():
	shuffleTest(MAX_M, MAX_N)