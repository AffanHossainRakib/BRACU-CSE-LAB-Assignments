from collections import defaultdict
import heapq

class Graph:
    def __init__(self, N):
        self.N = N
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v, w):
        self.graph[u].append((v,w))

    def dijkstra(self, s):
        visited = [0]*(self.N+1)
        distance = [float("INF")]*(self.N+1)
        distance[s] = 0
        pq = [(0,s)]

        while pq:
            u_weight, u = heapq.heappop(pq)
            if not visited[u]: 
                visited[u] = 1  
                for v, w in self.graph[u]:
                    if distance[v] > distance[u] + w:
                        distance[v] = distance[u] + w
                        heapq.heappush(pq, (w,v))
        return distance

    def shortestpath(self, s):
        distance = self.dijkstra(s)

        for i in range(1,self.N+1):
            if distance[i] == float("Inf"):
                output_file.write(f"{-1} ")
            else:
                output_file.write(f"{distance[i]} ")        


input_file = open("input1_1.txt", 'r')
output_file = open("output1_1.txt", 'w')

N, M = map(int, input_file.readline().split())
G = Graph(N)

for _ in range(M):
    u, v, w = map(int, input_file.readline().split())
    G.addEdge(u, v, w)

s = int(input_file.readline())
G.shortestpath(s)