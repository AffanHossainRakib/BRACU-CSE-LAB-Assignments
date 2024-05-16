class Graph:
    def __init__(self, N):
        self.N = N
        self.edges = []
        self.rank = [1 for i in range(self.N+1)]
        self.parent = [i for i in range(self.N+1)]
        self.cost = 0
    
    def addEdge(self, u, v, w):
        self.edges.append((w, u, v))

    def find_parent(self, r):
        if self.parent[r] == r:
            return r
        self.parent[r] = self.find_parent(self.parent[r])
        return self.parent[r]

    def union(self, a, b, w):
        par_a = self.find_parent(a)
        par_b = self.find_parent(b)

        if par_a != par_b:
            if self.rank[par_a] >= self.rank[par_b]:
                self.rank[par_a] += self.rank[par_b]
                self.parent[par_b] = par_a
                self.cost += w
            else:
                self.rank[par_b] += self.rank[par_a]
                self.parent[par_a] = par_b
                self.cost += w
    
    def kruskal(self):
        sorted_edges = sorted(self.edges, key = lambda x: x[0])
        for w, u, v in sorted_edges:
            self.union(u, v, w)
        output_file.write(str(self.cost))

input_file = open("input2_2.txt", 'r')
output_file = open("output2_2.txt", 'w')
N, K = map(int, input_file.readline().split())
G = Graph(N)
for _ in range(K):
    u, v, w = map(int, input_file.readline().split())
    G.addEdge(u, v, w)
G.kruskal()
