from collections import defaultdict

class Kosaraju:
    def __init__(self, n):
        self.vertices = n
        self.colors = ['white'] * n
        self.graph = defaultdict(list)

    def addEdge(self, src, dest):
        self.graph[src].append(dest)

    def dfs(self, src, seen):
        seen[src] = True
        print(src, end = ' ')
        for i in self.graph[src]:
            if not seen[i]:
                self.dfs(i, seen)

    def fillStack(self, src, seen, seenStack):
        seen[src] = True
        for i in self.graph[src]:
            if not seen[i]:
                self.fillStack(i, seen, seenStack)
        stack.append(src)

    def transpose(self):
        transposeGraph = self.Kosaraju(self.vertices)
        for i in self.graph:
            for j in self.graph[i]:
                transposeGraph.addEdge(self, j, i)
        return transposeGraph

    def stronglyConnectedComponents(self):
        seen = [False] * self.vertices
        stack = []

        for i in range(self.vertices):
            if not seen[i]:
                self.fillStack(self, seen, stack)

        transposeGraph = self.transpose()
        seen = [False] * self.vertices

        while stack:
            top = stack.pop()
            if not seen[top]:
                transposeGraph.dfs()
                print("")

g = Kosaraju(8)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(2, 4)
g.addEdge(3, 0)
g.addEdge(4, 5)
g.addEdge(5, 6)
g.addEdge(6, 4)
g.addEdge(6, 7)
g.stronglyConnectedComponents()