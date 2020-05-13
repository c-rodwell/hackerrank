#version without checking if missing (not in values) child node already exiss in queue
#and not checking on dequeue if the state is in values either (since duplicates in stack would do this)

#constants
EndState = None #end state - start with this in values.
KillTheWorld = (EndState, -float('inf')) #losing outcome

class State:

	#from tuple
	def __init__(self, state):
		self.step, self.energy = state
		self.remembered_outcomes = None

	def as_tuple(self):
		return (self.step, self.energy)

	#return list of (newstate, reward) possible outcomes
	def outcomes(self, config):
		#cache solution
		if self.remembered_outcomes:
			return self.remembered_outcomes

		N, V, P = config
		if self.step == N:
			retval =  [(EndState, V[self.step-1])]
		else:
			newstep = self.step + 1

			#case 1 - get score but no energy
			case1_energy = self.energy
			case1_score = V[self.step-1]

			#case 2 - copy the energy value, no score
			case2_energy = P[self.step-1]
			case2_score = 0

			#then continue if energy still > 0, otherwise lose
			if case1_energy > 0:
				case1 = ((newstep, case1_energy - 1), case1_score)
			else:
				case1 = KillTheWorld

			if case2_energy > 0:
				case2 = ((newstep, case2_energy - 1), case2_score)
			else:
				case2 = KillTheWorld

			retval = [case1, case2]
		
		self.remembered_outcomes = retval
		return retval

	def child_states(self, config):
		return [newstate for (newstate, score) in self.outcomes(config)]

	#compute max value of the node
	#can only do this once all child notes are in values
	def max_value(self, config, values):
		possibilities = self.outcomes(config)
		scores = [reward + values[newstate] for (newstate, reward) in possibilities]
		return max(scores)

def iterative_max_value(config):
	start = (1,0)
	stack = [State(start)]
	values = {EndState: 0} #this prevents making a State object from EndState
	while stack:
		lastState = stack[-1]

		childStates = lastState.child_states(config)
		#if all child nodes were evaluated, can evaluate the current state - take it off stack, save value
		#otherwise, put all missing nodes on stack
		missing = [state for state in childStates if state not in values]
		if missing:
			for state in missing:
					stack.append(State(state))
		else:
			stack.pop()
			values[lastState.as_tuple()] = lastState.max_value(config, values)
	return values[start]

def robot(vp):

    N = len(vp)
    V = []
    P = []
    for [vi, pi] in vp:
        V.append(vi)
        P.append(pi)
    
    config = (N,V,P)

    return iterative_max_value(config)