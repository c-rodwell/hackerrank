#straight runs approach: identify the strictly increasing or strictly decreasing runs
#straight run of length k will have candy amounts 1...k with total candy k(k+1)/2
#run ends when it switches between increasing or decreasing.
#also ends on a repeated rank - don't know what will happen after that
#states are 1 (increasing), -1 (decreasing), 0 (new run, not sure if increasing or decreasing yet)

#still can't get this to work, too many possible cases
#current problem: [3,4,3,1] returns 6, should be 7
#problem is it assumes ascending part [3,4] with length 2 will have candies 1+2 = 3,
#but actually the distribution is [1,3,2,1,2,3]  -> ascenting part [3,4] has total 4


def candies(n, arr):
	state = 0
	prev = arr[0]
	count = 1
	end = False
	total = 0
	for i in range(1, len(arr)):
		current = arr[i]
		if state == 0:
			if current > prev:
				state = 1
				count +=1
			if current < prev:
				state = -1
				count += 1
			if current == prev:
				end = True
				# total += count * (count+1)/2
				# count = 1
				# state = 0
		elif state == 1:
			if current > prev:
				count +=1
			else:
				end = True
				# total += count * (count+1)/2
				# count = 1
				# state = 0
		elif state == -1:
			if current < prev:
				count += 1
			else:
				end = True
			# elif current > prev:
			# 	#end = True
			# 	#special case - count the repeated 1 in count, but not in total.
			# 	total += count * (count+1)/2
			# 	total -= 1
			# 	count = 2
			# 	state = 0
			# else: #equal - end run, starts from 1 again
			# 	total += count * (count+1)/2
			# 	count = 1
			# 	state = 0
		if end:
			total += count * (count+1)/2
			count = 1
			if state == -1 and current > prev and (i == n -1  or arr[i+1] > current):
				#special case for overlapping 1 when decreasing run goes into increasing run
				#count from 2 instead, but subtract 1
				count += 1
				total -= 1
			state = 0
			end = False
		prev = current
	#add the last block at end of list
	total += count * (count+1)/2
	return int(total)