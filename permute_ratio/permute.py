#implement permutation instead of using itertools.permutations

#BASE = 10 #number system base, usually 10
#SIZE = 5 #size of each list: can be 1 up to BASE/2. usually 5

#generate all permutations from items of list, up to some length
def permute(items, length = None):
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

#could elminate permutations here which clearly wont work
#but for now use all of them.

#list of digits to integer.
def to_num(digitlist, BASE):
	length = len(digitlist)
	return sum(digit*pow(BASE, length-1-i) for i, digit in enumerate(digitlist))

def pairs(BASE, SIZE):
	digits = range(BASE)
	orderings = permute(digits,2*SIZE)
	solutions = []
	for order in orderings:
		p1 = order[:SIZE]
		p2 = order[SIZE:]
		n1 = to_num(p1, BASE)
		n2 = to_num(p2, BASE)
		if n1 % n2 == 0:
			solutions.append((n1, n2, n1//n2))
	solutions.sort(key=lambda x: x[2])
	return solutions