class Node:
    def __init__(self, v):
        self.vertex = v
        self.next = None

class Graph:
    def __init__(self, size):
        self.v = size# number of vertices in graph
        self.graph = [None] * size

    def addEdge(self, s, d):
        node = Node(d)
        node.next = self.graph[s]# next of node will point to the head of list
        self.graph[s] = node# connecting the new node to the vertex

        node = Node(s)
        node.next = self.graph[d]
        self.graph[d] = node

    def printGraph(self):
        for i in range(self.v):# looping through the indices
            temp = self.graph[i]# linked list in the current index
            while temp:
                print(temp.vertex)
                temp = temp.next
            print()

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 3)

g.printGraph()