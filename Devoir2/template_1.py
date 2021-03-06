"""
    Student template for the third homework of LINMA1691 "Théorie des graphes".

    Authors : Devillez Henri
"""

import math
import heapq
    
def prim_mst(N, roads):
    """ 
    INPUT : 
        - N, the number of crossroads
        - roads, list of tuple (u, v, s) giving a road between u and v with satisfaction s
    OUTPUT :
        - return the maximal satisfaction that can be achieved
        
        See homework statement for more details
    """
    total_satisfaction = 0
    satisfaction = 0
    
    adj = {i: [] for i in range(N)}
    for u, v, s in roads:
        adj[u].append([v, s])
        adj[v].append([u, s])
        total_satisfaction += s
    explored = set()            # Set of vertices in tree
    start = next(iter(adj))   # Arbitrary starting vertex
    for i in adj:
        print(i)
    unexplored = [(0, start)] 
    while unexplored:
        cost, winner = heapq.heappop(unexplored)
        if winner not in explored:
            explored.add(winner)
            satisfaction += cost
            for neighbour, cost in adj[winner]:
                if neighbour not in explored:
                    heapq.heappush(unexplored, (cost, neighbour))
    return total_satisfaction - satisfaction

    
if __name__ == "__main__":

    # Read Input for the first exercice
    
    with open('in1.txt', 'r') as fd:
        l = fd.readline()
        l = l.rstrip().split(' ')
        
        n, m = int(l[0]), int(l[1])
        
        roads = []
        for road in range(m):
        
            l = fd.readline().rstrip().split()
            roads.append(tuple([int(x) for x in l]))
            
    # Compute answer for the first exercice
     
    ans1 = prim_mst(n, roads)
     
    # Check results for the first exercice

    with open('out1.txt', 'r') as fd:
        l_output = fd.readline()
        expected_output = int(l_output)
        
        if expected_output == ans1:
            print("Exercice 1 : Correct")
        else:
            print("Exercice 1 : Wrong answer")
            print("Your output : %d ; Correct answer : %d" % (ans1, expected_output)) 
        

