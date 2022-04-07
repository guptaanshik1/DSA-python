class Graph:
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for j in range(size)])

    def addEdge(self, v1, v2):
        if v1 == v2:# like v1 v1 has 0 in matrix
            print("Both the vertices are same")
            return

        self.adjMatrix[v1][v2] = 1# if there is an edge from v1 to v2 then reverse is also possible
        self.adjMatrix[v2][v1] = 1

    def removeEdge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("There is no edge between v1 and v2")
            return

        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def printMatrix(self):
        for row in self.adjMatrix:
            print(row)

graph = Graph(4)# 4 is number of vertices

graph.addEdge(0, 1)# v0 to v1 and v1 to v0
graph.addEdge(1, 2)# v1 to v2 and v2 to v1
graph.addEdge(0, 2)# v0 to v2 and v2 to v0
graph.addEdge(2, 3)# v2 to v3 and v3 to v2

graph.printMatrix()