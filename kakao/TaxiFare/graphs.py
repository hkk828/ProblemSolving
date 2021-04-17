class Graph:
    def __init__(self, n, s, a, b, result, fares):
        self.n = n              # number of nodes in a graph
        self.s = s              # source node
        self.a = a              # target A
        self.b = b              # target B
        self.fares = fares      # fares information
        self.result = result    # minimum cost from source to A and B

graph1 = Graph(6, 4, 6, 2, 82, [[4, 1, 10],
                                [3, 5, 24],
                                [5, 6, 2],
                                [3, 1, 41],
                                [5, 1, 24],
                                [4, 6, 50],
                                [2, 4, 66],
                                [2, 3, 22],
                                [1, 6, 25]])

graph2 = Graph(7, 3, 4, 1, 14, [[5, 7, 9],
                                [4, 6, 4],
                                [3, 6, 1],
                                [3, 2, 3],
                                [2, 1, 6]])

graph3 = Graph(6, 4, 5, 6, 18, [[2, 6, 6],
                                [6, 3, 7],
                                [4, 6, 7],
                                [6, 5, 11],
                                [2, 5, 12],
                                [5, 3, 20],
                                [2, 4, 8],
                                [4, 3, 9]])