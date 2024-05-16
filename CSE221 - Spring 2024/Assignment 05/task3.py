from collections import defaultdict

class Graph:
    def __init__(self, N):
        self.N = N
        self.grpah = defaultdict(list)
        self.rev_graph = defaultdict(list)
        self.DISCOMP = []

    def addEdge(self, u, v):
        self.grpah[u].append(v)
        self.rev_graph[v].append(u)
    
    def step1(self):
        topo_stack = []
        visited = [0]*(self.N+1)
        for v in range(1, self.N+1):
            if not visited[v]:
                self.step2(v, visited, topo_stack)
        print(topo_stack)
        self.step3(topo_stack)

        for i in self.DISCOMP:
            for j in i:
                output_file.write(f"{j} ")
            output_file.write(f"\n")
    
    def step2(self, v, visited, topo_stack):
        visited[v] = 1
        for u in self.grpah[v]:
            if not visited[u]:
                self.step2(u, visited, topo_stack)
        topo_stack.append(v)
    
    def step3(self, topo_stack):
        visited = [0]*(self.N+1)
        
        for i in range(len(topo_stack)-1, -1, -1):
            v = topo_stack[i]
            temp = []
            if not visited[v]:
                self.DISCOMP.append(self.step4(v, visited, temp))

    def step4(self, v, visited, temp):
        visited[v] = 1
        temp.append(v)
        for u in self.rev_graph[v]:
            if not visited[u]:
                self.step4(u, visited, temp)
        return temp
    
    


    
input_file = open("input3_1.txt",'r')
output_file = open("output3_1.txt",'w')

N, M = map(int, input_file.readline().split())
G = Graph(N)
for _ in range(M):
    u, v = map(int, input_file.readline().split())
    G.addEdge(u,v)

G.step1()
input_file.close()
output_file.close()