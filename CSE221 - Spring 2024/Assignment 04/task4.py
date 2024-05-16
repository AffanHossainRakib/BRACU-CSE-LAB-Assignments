from collections import defaultdict

class Graph:
    def __init__(self, N):
        self.graph = defaultdict(list)
        self.N = N
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def isCycle(self):
        visited = [0 for i in range(self.N+1)]
        path = [0 for i in range(self.N+1)]

        for u in range(1, self.N+1):
            if not visited[u]:
                if self.isCycleUtil(u, visited, path):
                    return True
        return False
    
    def isCycleUtil(self, u, visited, path):
        visited[u] = 1
        path[u] = 1

        for v in self.graph[u]:
            if not visited[v]:
                if self.isCycleUtil(v, visited, path):
                    return True
            elif path[v]:
                return True
            
        path[u] = 0
        return False

input_file = open("input4_3.txt", 'r')
output_file = open("output4_3.txt", 'w')

N, M = map(int, input_file.readline().split())
G = Graph(N)
for _ in range(M):
    u, v = map(int, input_file.readline().split())
    G.addEdge(u,v)

if G.isCycle():
    output_file.write("YES")
else:
    output_file.write("NO")

input_file.close()
output_file.close()