import itertools

#BASE = 10 #number system base, usually 10
#SIZE = 5 #size of each list: can be 1 up to BASE/2. usually 5

#could elminate permutations here which clearly wont work
#but for now use all of them.

#list of digits to integer.
def to_num(digitlist, BASE):
	length = len(digitlist)
	return sum(digit*pow(BASE, length-1-i) for i, digit in enumerate(digitlist))

def pairs(BASE, SIZE):
	digits = range(BASE) #[0,1,2,3,4,5,6,7,8,9]
	orderings = itertools.permutations(digits,2*SIZE)
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