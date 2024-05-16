from collections import defaultdict
class Graph:
    def __init__(self, N):
        self.graph = defaultdict(list)
        self.N = N
    
    def addEdge(self, u, v):    
        self.graph[u].append(v)
    
    def pre_req(self):
        self.cycle = False
        stack = []

        visited = [0]*(self.N+1)
        path = [0]*(self.N+1) #cycle

        for v in range(1, self.N+1):
            if not self.cycle and not visited[v]:   
                self.DFS(v, visited, path, stack)
                
        if self.cycle:
            output_file.write("IMPOSSIBLE")
        else:
            while len(stack): 
                output_file.write(f"{stack.pop()} ")

    def DFS(self, v, visited, path, stack):
        visited[v], path[v] = 1, 1

        for u in self.graph[v]:
            if not visited[u]:  
                self.DFS(u, visited, path, stack)
            elif path[u] == 1:  
                self.cycle = True
        
        path[v] = 0   
        stack.append(v)

input_file = open("input1a_3.txt",'r')
output_file = open("output1a_3.txt",'w')

N, M = map(int, input_file.readline().split())
G = Graph(N)
for _ in range(M):
    u, v = map(int, input_file.readline().split())
    G.addEdge(u,v)
G.pre_req()

input_file.close()
output_file.close()