#this way finds the optimal distribution, then sum it.
#comprehensions version - use list comprehensions to reduce loops

def candies(n,arr):
	return sum(distribution(n,arr))

def distribution(n, arr):
	currentCandies = [1 for i in range(n)]
	nextCandies = None
	changed = True

	#keep going until no change. alternative is always do n iterations.
	while changed:
		first = currentCandies[0] + 1 if (arr[0] > arr[1] and currentCandies[0] <= currentCandies[1]) else currentCandies[0]
		last = currentCandies[n-1] +1 if (arr[n-1] > arr[n-2] and currentCandies[n-1] <= currentCandies[n-2]) else currentCandies[n-1]
		middle = [currentCandies[i]+1 if (arr[i] > arr[i-1] and currentCandies[i] <= currentCandies[i-1]) or (arr[i] > arr[i+1] and currentCandies[i] <= currentCandies[i+1])  else currentCandies[i] for i in range(1,n-1)]
		nextCandies = [first] + middle + [last] 
		changed = nextCandies != currentCandies
		currentCandies = nextCandies
	return currentCandies