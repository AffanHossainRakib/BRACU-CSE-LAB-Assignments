from collections import defaultdict
class Graph:
    def __init__(self, N):
        self.N = N
        self.graph = defaultdict(list)
        self.in_degree = [0]*(self.N+1)

    def addEdge(self, u, v):    
        self.graph[u].append(v)
        self.in_degree[v] += 1
    
    def pre_req_bfs(self):
        queue = []
        topo = []
        for v in range(1, self.N+1):
            if self.in_degree[v] == 0:
                queue.append(v)

        while len(queue):
            front = queue.pop(0)
            topo.append(front)

            for u in self.graph[front]:
                self.in_degree[u] -= 1
                if self.in_degree[u] == 0:
                    queue.append(u)
        
        if len(topo) == self.N:
            while len(topo): 
                output_file.write(f"{topo.pop(0)} ")
        else: 
            output_file.write("IMPOSSIBLE")

        
input_file = open("input1b_2.txt",'r')
output_file = open("output1b_2.txt",'w')

N, M = map(int, input_file.readline().split())
G = Graph(N)
for _ in range(M):
    u, v = map(int, input_file.readline().split())
    G.addEdge(u,v)

G.pre_req_bfs()
input_file.close()
output_file.close()