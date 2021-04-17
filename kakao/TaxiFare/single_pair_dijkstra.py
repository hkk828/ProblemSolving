from heapq import heappop, heappush

# Given a graph, a source node, and a target node,
# return a length of a shortest path from source to target, and the path
def single_pair_dijkstra(graph, source, target):
    visited = set()     # check visited nodes
    distance = [float('inf') for _ in range(len(graph))]
    distance[0] = None  # first element is dummy
    prev = {}           # key=Node, value=previous Node in a optimal path from source to key Node

    distance[source] = 0    # 0 distance from src to src
    prev[source] = None     # source has no previous node
    
    # explore a path
    search_heap = [(distance[source], source)]  # priority queue
    while search_heap and target not in visited:
        current_dist, current_node = heappop(search_heap)   # get current minimum distance from source and a node

        for neighbor_edge_pair in graph[current_node]:      # for each (neighbor, edge_cost) of current_node
            neighbor, edge_cost = neighbor_edge_pair        # split it
            new_dist = current_dist + edge_cost             # get new distance from source

            if new_dist < distance[neighbor]:               # if the new distance is shorter, then update it 
                distance[neighbor] = new_dist
                prev[neighbor] = current_node               # and mark current_node as a previous node of neighbor

            if neighbor not in visited and (distance[neighbor], neighbor) not in search_heap:   # if a neighbor has not been visited and not in the search_heap
                heappush(search_heap, (distance[neighbor], neighbor))                           # then add a pair (distance of neighbor, neighbor) in the heap
        visited.add(current_node)   # mark current_node as visited

    # if the target is not visited, then it is impossible to reach from the source
    # return infinity and empty list
    if target not in visited:
        return float('inf'), []

    # get intermediate nodes in a shortest path in reversed order
    path = [target]
    prev_node = prev[target]
    while prev_node:
        path.append(prev_node)
        prev_node = prev[prev_node]
    return distance[target], path[::-1]