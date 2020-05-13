#version of robot_forward using list comprehensions
#this is supposed to be faster than looping over lists.

def best_total_score(config):
	N, V, P = config
	routes = [(0,0)] #start state is step = 1(implied), energy = 0, accumulated score = 0
	for step in range(1,N): #step = 1 through step = N - 1 : 2 cases, lose if energy becomes 0
		
		#all routes fail - will happen if P has 0 at beginning, or too many 0 in a row.
		if not routes:
			print("all routes failed")
			return None

		#newRoutes = []
		
		this_score = V[step-1]
		this_energy = P[step-1]

		# make the +r options for each: same energy, increased max score by V[step]
		# results : one per previous tuple
		# for (energy, route_max_score) in routes:
		# 	if energy > 0: #otherwise that route fails, 
		# 		newRoutes.append((energy-1, route_max_score+this_score)) #could check energy > 0 here


		newRoutes = [(energy-1, route_max_score+this_score) for (energy, route_max_score) in routes if energy > 0]

		#make the "take energy" option: replace energy with P[step], no score increase
		#results: one entry, score is max of the previous tuple scores.
		all_max_score = max([route_max_score for (energy, route_max_score) in routes])
		if this_energy > 0: #can fail here if energy is 0
			newRoutes.append((this_energy-1, all_max_score))

		routes = newRoutes

		#prune all routes with energy = 0
		#subtract 1 energy for all the routes - this is after energy > 0 check.
		#write back all new values - or maybe pass in variable to next step without storing whole array

	#step = N: only the plus score case, no energy >0 check
	#newRoutes = []
	this_score = V[N-1]

	# for (energy, route_max_score) in routes:
	# 	newRoutes.append((energy-1, route_max_score+this_score))
	
	#routes = [(energy-1, route_max_score+this_score) for (energy, route_max_score) in routes]

	#then take highest score
	#return max(score for (energy, score) in routes)
	return max(route_max_score for (energy, route_max_score) in routes) + this_score


def robot(vp):

    N = len(vp)
    V = []
    P = []
    for [vi, pi] in vp:
        V.append(vi)
        P.append(pi)
    
    config = (N,V,P)

    return best_total_score(config)