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
		first = currentCandies[0] + 1 if wrongOrder(0,1,arr,currentCandies) else currentCandies[0]
		last = currentCandies[n-1] +1 if wrongOrder(n-1, n-2, arr, currentCandies) else currentCandies[n-1]
		middle = [currentCandies[i]+1 if wrongOrder(i, i-1, arr, currentCandies) or wrongOrder(i, i+1, arr, currentCandies) else currentCandies[i] for i in range(1,n-1)]
		nextCandies = [first] + middle + [last] 

		changed = nextCandies != currentCandies
		currentCandies = nextCandies
	return currentCandies

def wrongOrder(n1, n2, ratings, currentCandies):
	return ratings[n1] > ratings[n2] and currentCandies[n1] <= currentCandies[n2]