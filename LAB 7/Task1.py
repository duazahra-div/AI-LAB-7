class DepthLimitedSearch:

    def __init__(self, graph):
        self.graph = graph
        self.visited = []

    def DLS(self, node, goal, limit, path):

        self.visited.append(node)

        if node == goal:
            return path + [node]

        if limit <= 0:
            return None

        for child in self.graph[node]:

            result = self.DLS(child,goal,limit - 1,path + [node])

            if result is not None:
                return result

        return None


# Graph
graph = {
    'A': ['B', 'F', 'D', 'E'],
    'B': ['K', 'J'],
    'K': ['N', 'M'],
    'F': [],
    'D': ['G'],
    'E': ['C', 'H', 'I'],
    'G': [],
    'J': [],
    'N': [],
    'M': [],
    'C': [],
    'H': [],
    'I': ['L'],
    'L': []
}


# Object of class
search = DepthLimitedSearch(graph)


# DLS call
result = search.DLS('A', 'G', 2, [])


# Output
print("Visited Nodes:", search.visited)

if result:
    print("Goal Found!")
    print("Path:", result)
else:
    print("Goal Not Found")

