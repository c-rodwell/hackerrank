import math
import time
import itertools

#permutations algorithms: generate all permutations on a list
#note the implementations use optional length arg differently, but should match at length=None
#havent fixed this since I'm mainly looking at the full list permutations

#my first idea- iterative, at iteration n we have all permutations of length n
#maybe inefficient since many nested loops 
def looping_permute(items, length = None):
	if length is None:
		length = len(items)
	elif length > len(items):
		raise ValueError("length parameter must be less than or equal to length of array")
	#permutations array: index i stores a list of all permutations of length i, i from 0 to length
	#base case: at length 0, the only permutation is empty tuple
	permutations = [[] for i in range(0, length+1)]
	permutations[0].append(())
	for i in range(1, length+1):
		for p in permutations[i-1]:
			for item in items:
				if item not in p:
					permutations[i].append(p+tuple([item]))
	return permutations[length]

#recursive approach: pick one element, then permute the rest.
#multiple choices for first: must try all of them
#permuting the rest generates a list: need to add first element to all of those

def recursive_permute(items, length=None):
	if length:
		return recursive_permute(items)
	#base case: empty list
	if not items:
		return [[]]
	output = []
	for item in items:
		remaining = items[:]
		remaining.remove(item)
		remaining_permutations = recursive_permute(remaining)
		output += [[item]+permutation for permutation in remaining_permutations]
	return output

#my attempt at permutations by swapping in place
#correct up to 5, but failing on 6
#not the same as Heap's algorithm which only does single swaps
def cycles_permute(items, length=None):
	if length is None:
		length = len(items)
	elif length > len(items):
		raise ValueError("length parameter must be less than or equal to length of array")
	#permuting one element does nothing
	if length <= 1:
		return [items[:]]
	out = []
	out += cycles_permute(items, length-1)
	direction =  -1
	for i in range(length - 1):
		#needds to be cycle_inplace here, not cycle_copy - that way permutation state carries across recursive calls
		cycle_inplace(items, length, direction)
		direction = - direction
		out += cycles_permute(items, length-1)
	return out

#cyclic permutation on first n elements of items
def cycle_inplace(items, n, direction):
	#cycle to right
	if direction > 0:
		tmp = items[n-1]
		for i in range(n-1, 0, -1):
			items[i] = items[i-1]
		items[0] = tmp
	else: #cycle to left
		tmp = items[0]
		for i in range(0, n-1, 1):
			items[i] = items[i+1]
		items[n-1] = tmp

# def cycle_copy(items,n,direction):
# 	new_items = items[:]
# 	cycle_inplace(new_items, n, direction)
# 	return new_items

#_______test methods:___________

#itertools.permutations() returns an iterable of tuples, which is probably better than my list of lists format
#turn that into a list of lists so I can check is_correct_permutations_list
def itertools_permutations(items, length=None):
	if length is None:
		length = len(items)
	elif length > len(items):
		raise ValueError("length parameter must be less than or equal to length of array")
	return [list(x) for x in itertools.permutations(items, length)]


#set for uniqueness checking of the list of permutations. input is a list of lists
def unique_elements(perm_list):
	return set([tuple(pattern) for pattern in perm_list])

#check if pattern is permutation of base
#sets of elements are the same -> they have the same elements, ignoring order
#lengths are the same -> no repetitions in pattern (assume base has no repetitions)
def is_permutation_of(pattern, base):
	return set(pattern) == set(base) and len(pattern) == len(base)

#check that all the items are permutations of a base list.
def all_are_permutations_of(candidate, base):
	for pattern in candidate:
		if not is_permutation_of(pattern, base):
			return False
	return True

#candidate is correct permutations list of the base list:
#	1. each element of candidate is a correct permutation of base sequence
#	2. candidate has no repeated elements
#	3. candidate has right number of elements, which is factorial of length of base
#	equivalently to 2 and 3: # elements in candidate, # unique elements in candidate, and factorial(len(base)) are all the same.
def is_correct_permutations_list(candidate, base):
	return all_are_permutations_of(candidate, base) and len(unique_elements(candidate)) == len(candidate) == math.factorial(len(base))


CURRENT_METHODS = [
	("looping permute", looping_permute),
	("recursive permute", recursive_permute),
	("recursive permute with cycles", cycles_permute),
	("itertools.permutations, as list of lists", itertools_permutations)
	]

BASE_SIZES = [1,2,3,4,5,6,7,10,15,20,25,30]

def compareAll(methods = CURRENT_METHODS, sizes = BASE_SIZES, showLen = 200):

	for size in sizes:
		print("\n_______________comparing size = "+str(size)+"_______________")
		base = [i for i in range(size)]
		print("base list = "+str(base))

		for name, method in methods:
			print("\n"+name+":")
			before = time.time()
			answer = method(base)
			elapsed = time.time() - before
			correct = is_correct_permutations_list(answer, base)
			if len(answer) < showLen:
				print("answer = "+str(answer))
			else:
				print("too long to show")
			print("correct = "+str(correct))			
			print("length = "+str(len(answer)))
			print("elapsed = "+str(elapsed))	