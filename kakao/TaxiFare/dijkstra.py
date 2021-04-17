# given a list "graph" representing a graph G,
# such that graph[u] = [(v, d_uv) for v neighbor of u and d_uv is the cost of the edge], (nodes are represented as positive integers)
# and a source node "src",
# dijkstra returns a list of shortest distances from src to a node represented by its index.

from heapq import heappop, heappush

def dijkstra(graph, src):
    distance_from_src = [float('inf') for _ in range(len(graph))]
    distance_from_src[0] = None
    # 0 distance for src to src
    distance_from_src[src] = 0
    
    # loop while search heap is non-empty
    search_heap = [(0, src)]
    while search_heap:
        temp_dist_from_src, node = heappop(search_heap)

        # if a temporary distance of a node from src is greater than distance_from_src[node],
        # then it means a smaller pair is added in the heap, so we ignore this case.
        if distance_from_src[node] < temp_dist_from_src:
            continue

        for neighbor_edge_pair in graph[node]:                      # for each neighbor and edge_cost of node
            neighbor, edge_cost = neighbor_edge_pair                # split the pair (neighbor, edge_cost)
            new_dist_from_src = temp_dist_from_src + edge_cost      # calculate potential new distance from src to neighbor
            if new_dist_from_src < distance_from_src[neighbor]:     # if the new is smaller, update it
                distance_from_src[neighbor] = new_dist_from_src
            
            heappush(search_heap, (new_dist_from_src, neighbor))    # add new pair to the heap

    return distance_from_src