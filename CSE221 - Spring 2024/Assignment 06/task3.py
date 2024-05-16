from collections import defaultdict
import heapq

class Graph:
    def __init__(self, N) -> None:
        self.N =  N
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v, w):
        self.graph[u].append((v, w))

    def minimum_danger(self):
        visited = [0]*(self.N+1)
        danger = [float("INF")]*(self.N+1)
        danger[0] = float("-INF")

        parent = [-1]*(self.N+1)
        pq = [(0,1,0)]

        while pq:
            u_danger, u, par = heapq.heappop(pq)
            if u_danger < danger[u]:
                danger[u] = u_danger
                parent[u] = par

            if not visited[u]:
                visited[u] = 1
                for v, v_danger in self.graph[u]:
                    heapq.heappush(pq, (v_danger, v, u))
        
        self.file_writer(parent, danger)

    def file_writer(self, parent, danger):
        max_danger = 0

        if parent[self.N] == -1:
            max_danger = "Impossible"
        else:
            par = self.N
            while par != 1:
                max_danger = max(max_danger, danger[par])
                par = parent[par]
                
        output_file.write(str(max_danger))
            

input_file = open("input3_2.txt", 'r')
output_file = open("output3_2.txt", 'w')

N, M = map(int, input_file.readline().split())
G = Graph(N)

for _ in range(M):
    u, v, w = map(int, input_file.readline().split())
    G.addEdge(u, v, w)
G.minimum_danger()