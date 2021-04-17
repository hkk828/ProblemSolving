from dijkstra import dijkstra
from single_pair_dijkstra import single_pair_dijkstra

def get_taxi_fare(n, source, target_a, target_b, fares):

    graph = [[] for _ in range(n+1)]        # graph representation
    for fare in fares:                      # for each fare
        u, v, price = fare                  # save information on the graph
        graph[u].append((v, price))
        graph[v].append((u, price))

    d = [[None] * (n+1) for _ in range(n+1)]    # d[i][j] = minimum distance from i to j
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                d[i][j] = 0
            else:
                d[i][j] = single_pair_dijkstra(graph, i, j)[0] if not d[j][i] else d[j][i]

    min_fare = float('inf')
    for verge in range(1, n+1):     # for each verge (verge is a node where two people diverge)
                                    # get cost of (source-verge + verge-a + verge-b)
                                    # update if it is cheaper than minimum fare so far
        min_fare = min(min_fare, d[source][verge] + d[verge][target_a] + d[verge][target_b])
    return min_fare


if __name__ == '__main__':
    from graphs import graph1, graph2, graph3

    for graph in [graph1, graph2, graph3]:
        if get_taxi_fare(graph.n, graph.s, graph.a, graph.b, graph.fares) == graph.result:
            print("Passed a test case!")
        else:
            print("Failed a test case!")

