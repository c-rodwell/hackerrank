#"fibonacci modified" problem at https://www.hackerrank.com/challenges/fibonacci-modified/problem

#recurrence relation:	t_i+2 = t_i + (t_i+1)^2
#given t_1, t_2 and n, compute t_n

#I tried to find a direct formula for t_n but not sure how
# equivalent statement:	t_i = t_i-2 + t_i-1 ^ 2 is equivalent.
# if instead:	 		t_i = t_i-1 ^ 2 : then t_n = t_0 ^ (2 ^ n)
# 		t_n grows roughly as that function, but not exactly.

#try calculating each one t3 ... tn

def fib_modified(t1, t2, n):
	#given t1 and t2, calcualte t3, t4 ... tn. then return tn.
	# so calculation begins at t3
	# only need current and previous 2 values. compute latest, then shift down.
	minus1 = t2
	minus2 = t1
	latest = None
	
	for i in range(3,n+1):
		latest = (minus1 ** 2) + minus2
		minus2 = minus1
		minus1 = latest
	return latest

#this passed all tests on the hackerrank problem. I'm still curious if there is an exact formula but skipping for now.