import random #only for tests
import time #only for tests
import robot
import robot_tree_no_check
import robot_tree
import robot_tree_stack_contains
import robot_tree_wasqueued
import robot_forward
import robot_forward_comprehensions

start = (1,0)
conf1 = (4, [4,0,4,3], [2,2,0,4])


#random parameters in the hackerRank format, up to some maxes.
#bounds are 1 <= N <= 5x10^5, 0 <= Vi <= 10^9 , 0 <= Pi <= 10^5
#hackerrank input format is a [[v1, p1] ... [vn, pn]] list
def randomArgs(N, maxV, maxP):
    return [ [random.randint(0, maxV), random.randint(0, maxP)] for i in range(N)]

def testRandom(N, maxV, maxP):

    print("test for N = "+str(N)+", max V = "+str(maxV)+", max P = "+str(maxP))
    vp = randomArgs(N, maxV, maxP)
    #methods = [robot.robot, robot_tree.robot]
    # methods = [("no check for duplicates in stack", robot_tree_no_check.robot),
    #             ("check value exists on dequeue", robot_tree.robot),
    #             ("stack contains check before adding", robot_tree_stack_contains.robot),
    #             ("check stack contains with a set", robot_tree_wasqueued.robot),
    #             ("direct forward iteration", robot_forward.robot)]

    # methods = [("no check for duplicates in stack", robot_tree_no_check.robot),
    #             ("direct forward iteration", robot_forward.robot)]

    methods = [("direct forward iteration", robot_forward.robot), ("direct forward with comphrehensions", robot_forward_comprehensions.robot)]

    for name, function in methods:
        print("\nmethod: "+name)
        before = time.time()
        result = function(vp)
        elapsed = time.time() - before
        print("result = "+str(result))
        print("time = "+str(elapsed))