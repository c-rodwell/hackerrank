
# P sequence problem: https://www.hackerrank.com/challenges/p-sequences

# given arguments integers P and N, N >= 2, P >=1, find number of p-sequences modulo 10^9 + 7
#p-sequence: positive integer sequence of length N, where product of any 2 adjacent numbers is <= P
#ex for N=2, P=2: answwers are (1,1), (2,1), (1,2)	- count is 3

#try dynamic programming on list length

#to say which number can go next, only need the last number.

#sequences[k][i] : store all sequences of length k which end in number i, 1 <= i <= P

#for i = 1 to P:
#	buckets[1][i] = [[i]]
#for k = 2 to N:
#	for i = 1 to P:
#		for j = 1 to floor(P/i):
#			for seq in buckets[k-1][i]
#				buckets[k][j] . append (seq + j)
# combine buckets[N][1 to P] and return

#complexity:
#setup step: P
#loops: N * i = 1 to P * j = 1 to P/i  * sequencs in buckets
import math
import numpy
import time

def list_p_sequences(N,P):
	#print("\nlist_p_sequences: N = "+str(N)+", P = "+str(P))
	#setup data structure
	#sequences[k][j] will be list of sequences of length k ending in number j.

	#dictionary with N keys
	#print("\ninitialize empty structure")
	sequences = {}
	for k in range(1, N+1):
		sequences[k] = {}
		for j in range(1, P+1):
			sequences[k][j] = []
	#print('sequences:' +str(sequences))

	#for N=1, each number alone is a sequence
	#print("\nmake k = 1 sequences")
	for j in range(1, P+1):
		sequences[1][j].append([j])
	#print('sequences:' +str(sequences))

	#print("\niterate for k = 2 to N")
	for k in range(2, N+1):
		#print("k = "+str(k))
		for lastNum in range(1, P+1):
			#print("\tlastNum = "+str(lastNum))
			for nextNum in range(1, math.floor(P/lastNum)+1):
				#print("\t\tnextNum = "+str(nextNum))
				for seq in sequences[k-1][lastNum]:
					#print("\t\t\tseq = "+str(seq))
					newseq = seq + [nextNum]
					#print("\t\t\tnewseq = "+str(newseq))
					sequences[k][nextNum].append(newseq)
	#combine last layer and return
	output = sequences[N][1]
	for j in range(2, P+1):
		output += sequences[N][j]
	return output

#but the problem as posed is just to find the number of such sequences, not list them.
#one approach is to do the algorithm above, but just store counts instead of sequences:
#sequences[k][j] stores NUMBER of q-sequences of length k which end in letter j.

#for i = 1 to P:
#	buckets[1][i] = 1 	- only sequence is the number i alone
#for k = 2 to N:
#	for lastNum = 1 to P:
#		for newNum = 1 to floor(P/i):
#			buckets[k][j] += buckets[k-1][i]
# combine buckets[N][1 to P] and return

def count_p_sequences(N,P):
	#print("\ncount_p_sequences: N = "+str(N)+", P = "+str(P))
	#setup data structure
	#sequences[k][j] will store count of sequences of length k ending in number j.

	#dictionary with N keys
	#print("\ninitialize empty structure")
	sequences = {}
	for k in range(1, N+1):
		sequences[k] = {}
		for j in range(1, P+1):
			sequences[k][j] = 0
	#print('sequences:' +str(sequences))

	#for N=1, each number alone is a sequence
	#print("\nmake k = 1 sequences")
	for j in range(1, P+1):
		sequences[1][j] = 1
	#print('sequences:' +str(sequences))

	#print("\niterate for k = 2 to N")
	for k in range(2, N+1):
		#print("k = "+str(k))
		for lastNum in range(1, P+1):
			#print("\tlastNum = "+str(lastNum))
			for nextNum in range(1, math.floor(P/lastNum)+1):
				#print("\t\tnextNum = "+str(nextNum))
				count = sequences[k-1][lastNum]
				sequences[k][nextNum] += count
	#combine last layer and return
	output = sequences[N][1]
	for j in range(2, P+1):
		output += sequences[N][j]
	return output

def count_modulo_p_sequences(n,p):
	#hackerrank problem wants the answers modulo 
	modulus = pow(10,9)+7

	sequences = {}
	for k in range(1, n+1):
		sequences[k] = {}
		for j in range(1, p+1):
			sequences[k][j] = 0

	for j in range(1, p+1):
		sequences[1][j] = 1

	for k in range(2, n+1):
		for lastNum in range(1, p+1):
			for nextNum in range(1, math.floor(p/lastNum)+1):
				count = sequences[k-1][lastNum] 
				sequences[k][nextNum]  = (sequences[k][nextNum] + count) % modulus
	#combine last layer and return
	output = sequences[n][1]
	for j in range(2, p+1):
		output = (output + sequences[n][j]) % modulus
	return output

def count_modulo_p_sequences_list(n,p):
	#hackerrank problem wants the answers modulo 
	modulus = pow(10,9)+7

	sequences = [[0 for j in range(p)] for k in range(n)]
	for j in range(p):
		sequences[0][j] = 1

	for k in range(1, n):
		for lastNum in range(1, p+1):
			for nextNum in range(1, math.floor(p/lastNum)+1):
				count = sequences[k-1][lastNum-1] 
				sequences[k][nextNum-1]  = (sequences[k][nextNum-1] + count) % modulus
	#combine last layer and return
	output = sequences[n-1][0]
	for j in range(1, p):
		output = (output + sequences[n-1][j]) % modulus
	return output

#__________ Matrix Multiply- based methods __________

#using numpy, repeated matrix multiplication
def count_modulo_p_sequences_numpy(n,p):
	#hackerrank problem wants the answers modulo 
	modulus = pow(10,9)+7

	counts = numpy.zeros((n,p))
	for j in range(p):
		counts[0][j] = 1

	#matrix of which numbers can go after which.
	#zero indexed, so subtract one from the digit
	transitions = numpy.zeros((p,p))
	for digit_1 in range(1,p+1):
		for digit_2 in range(1,math.floor(p/digit_1)+1):
			transitions[digit_1 - 1][digit_2 - 1] = 1

	for k in range(1, n):

		counts[k] = numpy.matmul(transitions, counts[k-1]) % modulus

	#combine last layer and return
	output = counts[n-1][0]
	for j in range(1, p):
		output = (output + counts[n-1][j]) % modulus
	return output

#repeated matrix multiplication withoout numpy - use my own python matrix_vector_mul
def count_modulo_p_sequences_py_matmul(n,p):
	#hackerrank problem wants the answers modulo 
	modulus = pow(10,9)+7

	counts = [[0 for j in range(p)] for k in range(n)]
	for j in range(p):
		counts[0][j] = 1

	#matrix of which numbers can go after which.
	#zero indexed, so subtract one from the digit
	transitions = [[0 for j in range(p)] for k in range(p)]
	for digit_1 in range(1,p+1):
		for digit_2 in range(1,math.floor(p/digit_1)+1):
			transitions[digit_1 - 1][digit_2 - 1] = 1

	for k in range(1, n):
		counts[k] = matrix_vector_mul(transitions, counts[k-1], modulus)

	#combine last layer and return
	output = counts[n-1][0]
	for j in range(1, p):
		output = (output + counts[n-1][j]) % modulus
	return output

#multiply matrices in python - dont know any built-in way and hackerrank doesn't have numpy
#m is matrix in form of list of lists
#v is vector in form of list

def matrix_vector_mul(m,v):
	out = [0 for row in m]
	for i, row in enumerate(m):
		for j, val in enumerate(v):
			out[i] += m[i][j] * v[j]
	return out

def matrix_vector_mul(m,v, modulus):
	out = [0 for row in m]
	for i, row in enumerate(m):
		for j, val in enumerate(v):
			out[i] = (out[i] + m[i][j] * v[j]) % modulus
	return out

#__________ Matrix Power approaches - get transition matrix to (n-1) power __________

#with numpy built-in matrix power
def count_modulo_p_sequences_matrix_power_numpy(n,p):
	modulus = pow(10,9)+7

	counts_1 = numpy.ones(p)

	#matrix of which numbers can go after which.
	#zero indexed, so subtract one from the digit
	transitions = numpy.zeros((p,p))
	for digit_1 in range(1,p+1):
		for digit_2 in range(1,math.floor(p/digit_1)+1):
			transitions[digit_1 - 1][digit_2 - 1] = 1

	#now instead of multiiplying by transitions matrix n- times, take that matrix to the n-1 power.
	total_transition = numpy.linalg.matrix_power(transitions, n-1) % modulus
	counts_final = numpy.matmul(total_transition, counts_1) % modulus

	#combine last layer and return
	return sum(counts_final) % modulus
	# output = counts_final[0]
	# for j in range(1, p):
	# 	output = (output + counts_final[j]) % modulus
	# return output

#with my own modular matrix power, built on numpy matmul
def count_modulo_p_sequences_custom_matrix_power_numpy(n,p):
	modulus = pow(10,9)+7

	counts_1 = numpy.ones(p)

	#matrix of which numbers can go after which.
	#zero indexed, so subtract one from the digit
	transitions = numpy.zeros((p,p))
	for digit_1 in range(1,p+1):
		for digit_2 in range(1,math.floor(p/digit_1)+1):
			transitions[digit_1 - 1][digit_2 - 1] = 1

	#now instead of multiiplying by transitions matrix n- times, take that matrix to the n-1 power.
	total_transition = matrix_power_mod_numpy(transitions, n-1, modulus)
	counts_final = numpy.matmul(total_transition, counts_1) % modulus

	#combine last layer and return
	output = counts_final[0]
	for j in range(1, p):
		output = (output + counts_final[j]) % modulus
	return output

#with my own modular matrix power, no numpy
def count_modulo_p_sequences_custom_matrix_power_py(n,p):
	modulus = pow(10,9)+7

	counts_1 = [1 for i in range(p)]

	#matrix of which numbers can go after which.
	#zero indexed, so subtract one from the digit
	transitions = [[0 for j in range(p)] for k in range(p)]
	for digit_1 in range(1,p+1):
		for digit_2 in range(1,math.floor(p/digit_1)+1):
			transitions[digit_1 - 1][digit_2 - 1] = 1

	total_transition = matrix_power_mod_py(transitions, n-1, modulus)
	counts_final = matrix_vector_mul(total_transition, counts_1) % modulus

	#combine last layer and return
	output = counts_final[0]
	for j in range(1, p):
		output = (output + counts_final[j]) % modulus
	return output

#compute matrix m to a power, with modulus
def matrix_power_mod_numpy(m, power, modulus):
	#use repeated squaring
	#mod each time to keep values small
	#keep all the squares, then combine them to make the needed power

	biggest_power = 1
	biggest_matrix = m
	powers = {1:m}

	#find all matrix squares up to largest needed size
	while biggest_power <= power/2:
		biggest_power *= 2
		biggest_matrix = numpy.matmul(biggest_matrix, biggest_matrix) % modulus
		powers[biggest_power] = biggest_matrix

	#now we have all the squares - combine them into the needed power
	#multiply the squares from top down, just using the ones we need.

	output = numpy.eye(len(m))
	remainder = power
	while biggest_power >= 1:
		if remainder >= biggest_power:
			output = numpy.matmul(output, powers[biggest_power]) % modulus
			remainder -= biggest_power
		biggest_power /= 2
	return output

def matrix_power_mod_py(m, power, modulus):
	raise notImplemented

#test them - both should agree for same N,P

# args = [(2,2), (2,3), (3,2), (3,3), (4,2), (2,4), (3,4), (4,3), (2,5), (5,2), (3,5), (5,3)]
# for (n,p) in args:
# 	print("\nfor n = "+str(n)+", p = "+str(p)+":")
# 	sequences = list_p_sequences(n,p)
# 	print("sequences = "+str(sequences))
# 	print("length of that answer: "+str(len(sequences)))
# 	print("count = "+str(count_p_sequences(n,p)))

def calc_time(n,p):
	print("comparison for n = "+str(n)+", p = "+str(p))
	methods = [count_modulo_p_sequences, count_modulo_p_sequences_list, count_modulo_p_sequences_numpy, count_modulo_p_sequences_matrix_power_numpy, count_modulo_p_sequences_custom_matrix_power_numpy]
	for method in methods:
		before = time.time()
		count = method(n,p)
		elapsed = time.time() - before
		print("\nmethod: "+str(method))
		print("answer: "+str(count))
		print("time: "+str(elapsed))

def mult_time():
	return 0

