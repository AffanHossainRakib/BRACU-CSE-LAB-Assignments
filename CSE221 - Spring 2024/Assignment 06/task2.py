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

    def meetup(self, dis1, dis2):
        time = None
        node = None
        for i in range(1, self.N+1):
            if dis1[i] != float("inf") and dis2[i] != float("inf"):
                if time == None or max(dis1[i], dis2[i]) < time :
                    time = max(dis1[i], dis2[i])
                    node = i
        
        if time == None:
            output_file.write("Impossible")
        else:
            output_file.write(f"Time {time} \nNode {node}")

                    

input_file = open("input2_3.txt", 'r')
output_file = open("output2_3.txt", 'w')

N, M = map(int, input_file.readline().split())
G = Graph(N)

for _ in range(M):
    u, v, w = map(int, input_file.readline().split())
    G.addEdge(u, v, w)

s1, s2 = map(int, input_file.readline().split())
dis_1 = G.dijkstra(s1)
dis_2 = G.dijkstra(s2)
G.meetup(dis_1, dis_2)
