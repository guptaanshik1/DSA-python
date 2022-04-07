class Graph:
    def __init__(self, gdict):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEgde(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def bfs(self, vertex):
        visited = [vertex]#visited is a list containing first visited vertex
        queue = [vertex]
        while queue:
            deVertex = queue.pop(0)#first element removed from queue
            print(deVertex)
            for adjacentVertex in self.gdict[deVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)

    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            popVertex = stack.pop()#removing the top element of stack
            print(popVertex)
            for adjacentVertex in self.gdict[popVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    stack.append(adjacentVertex)


customDict = {
    # 'a': ['b', 'c'],
    # 'b': ['a', 'g'],
    # 'c': ['a', 'd'],
    # 'd': ['c', 'b'],
    # 'e': ['c', 'f'],
    # 'f': ['d', 'g'],
    # 'g': ['b', 'b']
    'a': ['b', 'c'],
    'b': ['a', 'd', 'e'],
    'c': ['a', 'e'],
    'd': ['b', 'e', 'f'],
    'e': ['f', 'd', 'e', 'b'],
    'f': ['d', 'e']
}

graph = Graph(customDict)
print(customDict)
print()
graph.addEgde("d", "f")
print(customDict)

print("\nBFS: ")
graph.bfs("a")
print("\nDFS: ")
graph.dfs("a")