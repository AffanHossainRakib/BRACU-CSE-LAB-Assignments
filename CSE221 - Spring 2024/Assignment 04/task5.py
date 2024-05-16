from collections import defaultdict

class Graph:
    def __init__(self, N) -> None:
        self.graph = defaultdict(list)
        self.N = N
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def shortestPath(self, destination):
        visited = [0 for i in range(self.N+1)]
        parent = [None for i in range(self.N+1)]
        level = [float("inf") for i in range(self.N+1)]

        q = [1]
        visited[1] = 1
        level[1] = 0
        
        while q:
            u = q.pop(0)
            for v in self.graph[u]:
                if not visited[v]:
                    visited[v] = 1
                    parent[v] = u
                    level[v] = level[parent[v]] + 1
                    q.append(v) 
                    
        self.fileWriter(destination, level, parent)
    def fileWriter(self, destination, level, parent):
        output_file.write(f"Time: {level[destination]}\n")

        shortest_path = []
        while destination != None:
            shortest_path.append(destination)
            destination = parent[destination]

        shortest_path.reverse()
        final_path = ""
        for i in shortest_path:
            final_path += str(i) + " "

        output_file.write(f"Shortest Path: {final_path}")

input_file = open("input5_5.txt", 'r')
output_file = open("output5_5.txt", 'w')

N, M, D = map(int, input_file.readline().split())
G = Graph(N)
for _ in range(M):
    u, v = map(int, input_file.readline().split())
    G.addEdge(u,v)

G.shortestPath(D)

input_file.close()
# output_file.close()

# a = [3, 43, 46, 43, 3290, 2, 4, 6, 7]
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)