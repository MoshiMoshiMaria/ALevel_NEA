from mapFile import dave
import random

graph = []
for x in dave.adjacencies:
    graph.append(x)
target = random.choice(graph)
nodeCount = len(dave.adjacencies)
print("Start:",graph[0])
print("Target:",target)
print("Node Count:",nodeCount)

def findPath(graph,start,target): #returns a path to the end node from the start node
    q = [[start]]
    visited = []
    if start == target:
        return "You are on your target"        
    while len(q) > 0:
        path = q.pop(0)
        node = path[-1]
        if node not in visited and node != "":
            adjacent = graph[node].split(";")
            for x in adjacent:
                tempPath = list(path)
                tempPath.append(x)
                q.append(tempPath)
                if x == target:
                    return tempPath

            visited.append(node)
            
print(findPath(dave.adjacencies,graph[0],target))

            
        
    
