from dijkstra import dijkstra
from heapq import heappush, heappop

def get_taxi_fare(n, s, a, b, fares):
    min_fare = float('inf')

    graph = [[] for _ in range(n + 1)]              # graph representation
    for source, target, edge_cost in fares:         # for each fare
        graph[source].append((target, edge_cost))   # save it on graph
        graph[target].append((source, edge_cost))
    
    for verge in range(1, n + 1):                   # for each verge (verge is a node where two people diverge)
        dist_from_verge = dijkstra(graph, verge)    # get costs of paths starting from verge
        min_fare = min(min_fare, dist_from_verge[s] + dist_from_verge[a] + dist_from_verge[b])  # get the final cost (s-verge + verge-a + verge-b)
    return min_fare

if __name__ == '__main__':
    from graphs import graph1, graph2, graph3

    for graph in [graph1, graph2, graph3]:
        if get_taxi_fare(graph.n, graph.s, graph.a, graph.b, graph.fares) == graph.result:
            print("Passed a test case!")
        else:
            print("Failed a test case!")