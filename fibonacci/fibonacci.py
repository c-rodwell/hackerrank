import functools
import math
import time

#not a hackerrank problem, just trying for my own interest.

#fibonacci sequence: f0 = 0, f1 = 1, fn = fn-1 + fn-2

#try some different ways to compute it and compare efficiency.


#naively write a recursive function since its a simple definition.
#but this should be really inefficient because of repeated sub-problems
#complexity of the function is roughly the fibonacci sequence itself (which is roughly exponential)
def fib_simple_recursive(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fib_simple_recursive(n-1) + fib_simple_recursive(n-2)

#built-in python method to memoize the same code.
@functools.lru_cache(maxsize=None)
def fib_simple_recursive_cache(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fib_simple_recursive_cache(n-1) + fib_simple_recursive_cache(n-2)

#implement memoizing with 2 functions
def fib_memoize_wrapper(n):
	memo = {0:0, 1:1} #memo table with base cases
	return fib_memoize_inner(memo, n)

def fib_memoize_inner(memo, n):
	if n in memo:
		return memo[n]
	answer = fib_memoize_inner(memo, n-1) + fib_memoize_inner(memo, n-2)
	memo[n] = answer
	return answer


#iterative: this is how you would do it on paper
#table starts from index 0 and we defined f0 = 0, f1 = 1.
#so we need to fill in indexes 2 through n
def fib_iter(n):
	table = [None for i in range(n+1)]
	table[0] = 0
	table[1] = 1
	for i in range(2,n+1):
		table[i] = table[i-1]+table[i-2]
	return table[n]


#direct calculation with exponential formula
#this should be the most efficient

#calculations involce irrational numbers even though answer is int - may have to optimize rounding calcs
#maybe just calculate the positive exponential and round to closest int

def fib_direct(n):
	b1 = (1.0 + math.sqrt(5))/2.0
	b2 = (1.0 - math.sqrt(5))/2.0
	coeff1 = 1.0/math.sqrt(5)
	coeff2 = - coeff1
	return coeff1 * pow(b1, n) + coeff2 * pow(b2, n)

def test(n):
	functions = {
		#"naive recursive":fib_simple_recursive,
		"built-in memoize":fib_simple_recursive_cache,
		"my own memoize":fib_memoize_wrapper,
		"iterative":fib_iter,
		"direct calculation by formula":fib_direct
	}
	print("comparing fibonacci calculators for n = "+str(n))
	for name in functions:
		print("\n"+name+":")
		func = functions[name]
		before = time.time()
		answer = func(n)
		elapsed = time.time() - before
		print("answer = "+str(answer))
		print("time = "+str(elapsed))


#results:
#naive recursive gets really slow even at small n.
#n = 25 in 0.05 s, 30 in  0.5 s, 35 in 5s, 40 in 50s - thats a nice exponential pattern
# 1.618^ 5 = 11.09  - so 10 times time for n=5 increase looks right.

#my own memoize approaches hit stack limit at n = 998
#built-in memoize starts hitting stack limit around n = 1500 or 2000, but inconsistent
	#calling repeatedly with n increasing by 100 each time seems to keep working without hitting stack limit
	#so the lru cache makes repeated calls more efficient, while my own memoize is only within one call of wrapper.

#direct calculation is fastest, but hits overflow at n = 1475
#at 1474: iterative took about 0.0001 usually (but sometimes 0), direct says 0

#iterative starts taking a long time around n = 10^5
# n = 100000  (hundred thousand) - answers in 0.45 seconds, really long answer.
# n = 1000000 (million )- long pause, then memory error
