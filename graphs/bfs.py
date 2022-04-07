class BFS:
    def __init__(self, vertices):
        self.dist = [0] * vertices
        self.pred = [-1] * vertices
        self.colors = ['White'] * vertices
        self.graph = {
            0: [1],
            1: [0, 2],
            2: [1, 3],
            3: [2, 4, 5],
            4: [3, 5, 7],
            5: [3, 4, 6, 7],
            6: [5, 7],
            7: [4, 5, 6]
        }

    def bfs(self, source):
        queue = []
        queue.append(source)

        self.dist[source] = 0# initially source vertex is 0
        self.colors[source] = 'Gray'# source vertex is enqueued so Gray

        while queue:
            dequeuedVertex = queue.pop(0)
            print("Vertex {}".format(dequeuedVertex))

            # looping through all adjacent vertices of dequeuedVertex i.e. 2: [1, 3]
            for i in range(len(self.graph[dequeuedVertex])):
                if self.colors[self.graph[dequeuedVertex][i]] == 'White':# means the vertex is unvisited
                    self.colors[self.graph[dequeuedVertex][i]] = 'Gray'
                    self.dist[self.graph[dequeuedVertex][i]] = self.dist[dequeuedVertex] + 1
                    # the adjacent vertices will dequeuedVertex as predecessor
                    self.pred[self.graph[dequeuedVertex][i]] = dequeuedVertex
                    queue.append(self.graph[dequeuedVertex][i])

            self.colors[dequeuedVertex] = 'Black'# means all the adjacent vertices to this vertex have been visited

b = BFS(8)
b.bfs(2)

# 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 git token