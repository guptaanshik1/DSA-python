from collections import defaultdict

class Graph:
    def __init__(self, numberOfVertices):
        self.graph = defaultdict(list)
        self.numberOfVertices = numberOfVertices

    def addEdge(self, vertex, edge):
       self.graph[vertex].append(edge)

    def topologicalSortUtil(self, currentVertex, visited, stack):
        visited.append(currentVertex)#the current vertex is visited
        for i in list(currentVertex):#checking for the adjacent vertices of currentVertex
            if i not in visited:
                topologicalSortUtil(i, visited, stack)

        stack.insert(0, currentVertex)

    def topologicalSort(self):
        visited = []
        stack = []
        for k in list(self.graph):
            if k not in visited:
                self.topologicalSortUtil(k, visited, stack)

        print(stack)

customGraph = Graph(8)
customGraph.addEdge('a', 'c')
customGraph.addEdge('c', 'e')
customGraph.addEdge('e', 'h')
customGraph.addEdge('e', 'f')
customGraph.addEdge('f', 'g')
customGraph.addEdge('b', 'd')
customGraph.addEdge('b', 'c')
customGraph.addEdge('d', 'f')

customGraph.topologicalSort()
