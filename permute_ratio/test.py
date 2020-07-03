import random
import time
import norefine
import permute

methods = [
	("itertools permutation", norefine.pairs),
	("implement permuation myself", permute.pairs)
	]

def compareAll(base, size):
	print("comparison for base = "+str(base)+", size = "+str(size))
	for name, method in methods:
		print("\n"+name+":")
		before = time.time()
		answer = method(base, size)
		elapsed = time.time() - before
		print("answer = "+str(answer))
		print("length = "+str(len(answer)))
		print("elapsed = "+str(elapsed))