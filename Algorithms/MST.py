def spanningTree(graph, n, e):
    """http://practice.geeksforgeeks.org/problems/minimum-spanning-tree/1"""
    distance = {i:1001 for i in range(n)}
    distance[0] = 0
    mstSize = 0

    while len(distance) > 0:
        minKey = min(distance,key = distance.get)
        if(distance[minKey] == 1001):
            return mstSize
        mstSize += distance[minKey]
        for j in range(n):
            edge = graph[minKey][j]
            if(edge > 0 and j in distance and edge < distance[j] and not j == minKey):
                distance[j] = edge
        del distance[minKey]
    return mstSize


