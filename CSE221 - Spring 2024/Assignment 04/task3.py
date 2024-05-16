from collections import defaultdict
class Graph:
    def __init__(self, N):
        self.graph = defaultdict(list)
        self.N = N
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def dfs(self, s):
        visited = [0 for i in range(self.N+1)]
        dfs_traverse = []
        self.dfs_util(s, visited, dfs_traverse)

        self.fileWriter(dfs_traverse)
        
    def dfs_util(self, u, visited, dfs_traverse):
        visited[u] = 1
        dfs_traverse.append(u)
        for v in self.graph[u]:
            if not visited[v]:
                self.dfs_util(v, visited, dfs_traverse)
    
    def fileWriter(self, arr):
        for i in arr:
            output_file.write(f"{i} ")



input_file = open("input3_4.txt", 'r')
output_file = open("output3_4.txt", 'w')

N, M = map(int, input_file.readline().split())
G = Graph(N)
for _ in range(M):
    u, v = map(int, input_file.readline().split())
    G.addEdge(u,v)

G.dfs(1)
input_file.close()
output_file.close()