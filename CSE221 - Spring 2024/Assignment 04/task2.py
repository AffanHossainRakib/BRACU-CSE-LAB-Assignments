from collections import defaultdict
class Graph:
    def __init__(self, N):
        self.graph = defaultdict(list)
        self.N = N

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def bfs(self, source):
        visited = [0 for i in range(self.N+1)]
        queue = [source]
        visited[source] = 1

        while len(queue) != 0:
            front = queue[0]
            queue.pop(0)
            output_file.write(f"{front} ")
            
            for i in self.graph[front]:
                if visited[i] == 0:
                    queue.append(i)
                    visited[i] = 1
            


input_file = open("input2_1.txt", 'r')
output_file = open("output2_1.txt", 'w')

N, M = map(int, input_file.readline().split())
G = Graph(N)
for _ in range(M):
    u, v = map(int, input_file.readline().split())
    G.addEdge(u,v)

G.bfs(1)
input_file.close()
output_file.close()