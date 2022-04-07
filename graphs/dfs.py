from collections import defaultdict

class DFS:
    def __init__(self, n):
        self.vertices = n
        self.colors = ['white'] * n
        # self.time = 0
        self.startTime = [0] * n
        self.endTime = [0] * n
        self.graph = defaultdict(list)# {0: [....]}

    def addEdge(self, u, v):
        self.graph[u].append(v)# appending the destination vertex in the list of source vertex
        # if u = 0, v = 1
        # {0: [1]}

    def dfs(self, u):
        for i in range(self.vertices):
            self.time = 0
            if self.colors[i] == 'white':
                self.dfsVisit(i)
        print(self.startTime)
        print(self.endTime)

    def dfsVisit(self, u):
        self.time += 1
        self.startTime[u] = self.time
        self.colors[u] = 'gray'
        print(u)
        
        for i in self.graph[u]:# looping through the adjacent vertices of the u vertex
            if self.colors[i] == 'white':
                self.dfsVisit(i)# if color of adjacent vertex is white then repeating above procedure
        
        self.time += 1
        self.endTime[u] = self.time
        self.colors[u] = 'black'

d = DFS(6)
d.addEdge(0, 1)
d.addEdge(0, 2)
d.addEdge(1, 2)
d.addEdge(2, 3)
d.addEdge(3, 1)
d.addEdge(4, 3)
d.addEdge(4, 5)
d.addEdge(5, 5)

d.dfs(0)