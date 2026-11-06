# Iterative Deepening Search (IDDFS) using Class

class IDDFS:

    def __init__(self):
        self.graph = {
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

    def DLS(self, node, goal, limit, path, visited):

        visited.append(node)

        if node == goal:
            return path + [node]

        if limit <= 0:
            return None

        for child in self.graph[node]:

            result = self.DLS(child,goal,limit - 1,path + [node],visited)

            if result is not None:
                return result

        return None


    def IDDFS(self, start, goal, max_depth):

        for depth in range(max_depth + 1):

            visited = []

            result = self.DLS(start,goal,depth,[],visited)

            print("Depth Limit:", depth)
            print("Visited Nodes:", visited)

            if result is not None:

                print("Goal Found!")
                print("Path:", result)

                return

        print("Goal Not Found")


# Object of class
search = IDDFS()

# Calling IDDFS
search.IDDFS('A', 'G', 5)