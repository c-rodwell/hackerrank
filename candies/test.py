import random
import time
import iter_multipass_inplace
import iter_scores_per_pass
import straight_runs
import iter_comprehensions
import iter_no_func

methods = [
	("iterative multipass, in-place", iter_multipass_inplace.candies),
	("iterative multipass, new scores per pass", iter_scores_per_pass.candies),
	("iterative multipass with comprehensions", iter_comprehensions.candies),
	("comprehensions, no separate wrong_order function", iter_no_func.candies)
	#("straight runs", straight_runs.candies)
	]

def compareAll(n, arr):
	print("comparison for n = "+str(n)+", arr = "+str(arr))
	for name, method in methods:
		print("\n"+name+":")
		before = time.time()
		answer = method(n, arr)
		elapsed = time.time() - before
		print("answer = "+str(answer))
		print("elapsed = "+str(elapsed))

#candies(3, [1,2,2]) = 4
def ex0():
	compareAll(3, [1,2,2])

#expect 19
def ex1():
	compareAll(10,[2,4,2,6,1,7,8,9,2,1])

#expect 12
def ex2():
	compareAll(8,[2,4,3,5,2,6,4,5])

#required range is 1 <= arr[i] <= 10^5, 1 <= n <= 10^5
MAX_N = pow(10,5)
MAX_ARR = pow(10,5)

def randomTest(n,max_arr):
	arr = [random.randint(1, max_arr) for x in range(n)]
	compareAll(n, arr)

def maxRequiredTest():
	randomTest(MAX_N, MAX_ARR)