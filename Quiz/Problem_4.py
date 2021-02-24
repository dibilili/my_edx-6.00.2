# Problem 4
#  Bookmark this page
# Problem 4
# 20.0/20.0 points (graded)
#You are given the following code. It has functions to create a random graph and 
#to find a path between two nodes. The graph is represented by a dictionary; integer 
#keys represent all the nodes in the graph; each key has a list of integers representing 
#the nodes that the key has a directed edge to. Assume the code in the provided functions
#meets the specifications given.
#  
#import random
#
#
## You are given this function - do not modify
#def createRandomGraph():
#    """Creates a digraph with 7 randomly chosen integer nodes from 0 to 9 and
#    randomly chosen directed edges (between 10 and 20 edges)
#    """
#    g = {}
#    n = random.sample([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 7)
#    for i in n:
#        g[i] = []
#    edges = random.randint(10, 20)
#    count = 0
#    while count < edges:
#        a = random.choice(n)
#        b = random.choice(n)
#        if #b not in g[a] and a != b:
#            g[a].append(b)
#            count += 1
#    return g
#
#
## You are given this function - do not modify
#def findPath(g, start, end, path=[]):
#    """ Uses DFS to find a path between a start and an end node in g.
#    If no path is found, returns None. If a path is found, returns the
#    list of nodes """
#    path = path + [start]
#    if start == end:
#        return path
#    if not start in g:
#        return None
#    for node in g[start]:
#        if node not in path:
#            newpath = findPath(g, node, end, path)
#            if newpath: return newpath
#    return None
#
#
##########################
### WRITE THIS FUNCTION ##
##########################        
#
#def allReachable(g, n):
#    """
#    Assumes g is a directed graph and n a node in g.
#    Returns a sorted list (increasing by node number) containing all 
#    nodes m such that there is a path from n to m in g. 
#    Does not include the node itself.
#    """
#    # TODO


# Write the missing function according to the specification.
'''def allReachable(g, n):
    """
    Assumes g is a directed graph and n a node in g.
    Returns a sorted list (increasing by node number) containing all 
    nodes m such that there is a path from n to m in g.
    Does not include the node itself.  
    """'''

def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    multipliers = []
    remain = s
    for i in L:
        if i <= remain:
            mult = remain // i
            multipliers.append(mult)
            remain -= i * mult
        else:
            multipliers.append(0)
    sum1 = 0
    for j in range(len(multipliers)):
        sum1 += L[j]*multipliers[j]
    if sum1 == s:
        return sum(multipliers)
    else:
        return 'no solution'
        
# correctCorrect
