#this way finds the optimal distribution, then sum it.

def candies(n,arr):
	return sum(distribution(n,arr))

def distribution(n, arr):
	currentCandies = [1 for i in range(n)]
	changed = True
	while changed:
		changed = False
		nextCandies = currentCandies[:]
		#if higher ranking than either neighbor but doesn't have more candy, get one more candy
		#i=0 and i=n-1 cases are different since one neighbor
		if wrongOrder(0, 1, arr, currentCandies):
			nextCandies[0] += 1
			changed = True
		for i in range(1,n-1):
			if wrongOrder(i, i-1, arr, currentCandies) or wrongOrder(i, i+1, arr, currentCandies):
				nextCandies[i] += 1
				changed = True
		if wrongOrder(n-1, n-2, arr, currentCandies):
			nextCandies[n-1] += 1
			changed = True
		currentCandies = nextCandies
	return currentCandies

def wrongOrder(n1, n2, ratings, currentCandies):
	return ratings[n1] > ratings[n2] and currentCandies[n1] <= currentCandies[n2]