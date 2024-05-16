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
    
    def step_1(self):
        topo_stack = []
        visited = [0 for i in range(self.N+1)]

        for u in range(1, self.N+1):
            if not visited[u]:
                self.step_2(u, visited, topo_stack)
        # print(topo_stack)
        # print(visited)
        self.step_3(topo_stack)

    def step_2(self, u, visited, topo_stack):
        visited[u] = 1
        for v in self.grpah[u]:
            if not visited[v]:
                self.step_2(v, visited, topo_stack)

        topo_stack.append(u)
    
    def step_3(self, topo_stack):
        visited = [0 for i in range(self.N+1)]
        for i in range(len(topo_stack)-1, -1, -1):
            u = topo_stack[i]
            temp = []
            if not visited[u]:
                pass

    def step_4(self, u, visited, )



input_file = open("input3_1.txt",'r')
output_file = open("output3_1.txt",'w')

N, M = map(int, input_file.readline().split())
G = Graph(N)
for _ in range(M):
    u, v = map(int, input_file.readline().split())
    G.addEdge(u,v)

G.step_1()

input_file.close()
output_file.close()

