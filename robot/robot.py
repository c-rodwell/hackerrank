EndState = None
KillTheWorld = (EndState, -float('inf'))

def outcomes(oldstate, config):
    #end of list- only outcome is get reward V[N], then done
    step, energy = oldstate
    N, V, P = config
    if step == N:
        return [(EndState, V[step-1])]
    else:
        newstep = step + 1

        #case 1 - get score but no energy
        case1_energy = energy
        case1_score = V[step-1]

        #case 2 - copy the energy value, no score
        case2_energy = P[step-1]
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

        return [case1, case2]

#recursively find max reward of a state.
#check that memo is passed correctly so other scopes see memoized values
def max_score(state, config, memo):

    #print("\nmax score on state = "+str(state)+", memo = "+str(memo))

    #memoize state values
    if state in memo:
        return memo[state]

    #value is cumulative, so end state has value 0
    if state is EndState:
        return 0

    possibilities = outcomes(state, config)

    scores = [reward + max_score(newstate, config, memo) for (newstate, reward) in possibilities]
    best = max(scores)

    #store solution
    memo[state] = best
    #print("adding value "+str(best)+" to memo for state = "+str(state))
    #print("now memo is "+str(memo))
    return best


#get args from hackerrank problem and call my function:

def robot(vp):

    N = len(vp)
    V = []
    P = []
    for [vi, pi] in vp:
        V.append(vi)
        P.append(pi)
    
    start = (1,0)
    config = (N,V,P)
    memo = {}

    return max_score(start, config, memo)
