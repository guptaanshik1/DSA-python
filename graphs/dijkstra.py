from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def addNode(self, value):
        self.nodes.add(value)

    def addEdge(self, fromNode, toNode, distance):
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode, toNode)] = distance

def dijkstra(graph, initial):
    visited: {initial: 0}
    path = defaultdict(list)
    nodes = set(graph.nodes)

    while nodes:
        minNode = None
        for node in nodes:
            minNode = node
            if visited[node] < visited[minNode]:
                minNode = node
            if minNode is none:
                break
            nodes.remove(minNode)
            currentWeight = visited[minNode]
            print(currentWeight)

customGraph = Graph()
customGraph.addNode("A")
customGraph.addNode("B")
customGraph.addNode("C")
customGraph.addNode("D")
customGraph.addNode("E")
customGraph.addNode("F")
customGraph.addNode("G")

customGraph.addEdge("A", "B", 2)
customGraph.addEdge("A", "C", 5)
customGraph.addEdge("B", "C", 6)
customGraph.addEdge("B", "D", 1)
customGraph.addEdge("B", "E", 3)
customGraph.addEdge("C", "F", 8)
customGraph.addEdge("D", "E", 4)
customGraph.addEdge("E", "G", 9)
customGraph.addEdge("F", "G", 8)

dijkstra(customGraph, "A")


