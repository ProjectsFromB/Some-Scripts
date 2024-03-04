from itertools import permutations

def findDistance(graph, src):
    n = len(graph)
    distance = [float('inf')] * n
    distance[src] = 0
    for i in range(n):
        for u in range(n):
            for v in range(n):
                weight = graph[u][v]
                if distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight
    return distance

def bellmanFord(graph):
    distances = []
    for vertex in range(len(graph)):
        distances.append(findDistance(graph, vertex))
    return distances

def negativeCycle(graph):
    distance = graph[0]
    n = len(graph)
    for u in range(n):
        for v in range(n):
            weight = graph[u][v]
            if distance[u] + weight < distance[v]:
                return True
    return False

def getPathTime(bunnies, graph):
    time = 0
    time += graph[0][bunnies[0]]
    time += graph[bunnies[-1]][len(graph) - 1]
    for i in range(1, len(bunnies)):
        u = bunnies[i - 1]
        v = bunnies[i]
        time += graph[u][v]
    return time

def solution(times, time_limit):
    n_bunnies = len(times) - 2
    bunnies = [x for x in range(1, n_bunnies + 1)]
    distances = bellmanFord(times)
    if negativeCycle(distances):
        return range(n_bunnies)

    for i in range(n_bunnies, 0, -1):
        for perm in permutations(bunnies, i):
            time = getPathTime(perm, distances)
            if time <= time_limit:
                return [x - 1 for x in sorted(perm)]
    return []

