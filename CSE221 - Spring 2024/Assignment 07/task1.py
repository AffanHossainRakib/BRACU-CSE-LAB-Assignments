class disjointSet:
    def __init__(self, N):
        self.N = N
        self.rank = [1 for i in range(N+1)]
        self.parent = [i for i in range(N+1)]

    def find_parent(self, r):
        if self.parent[r] == r:
            return r
        self.parent[r] = self.find_parent(self.parent[r])
        return self.parent[r]
    
    def union(self, a, b):
        par_a = self.find_parent(a)
        par_b = self.find_parent(b)

        if par_a != par_b:
            if self.rank[par_a] >= self.rank[par_b]:
                self.rank[par_a] += self.rank[par_b]
                self.parent[par_b] = par_a
                output = self.rank[par_a]
            else:
                self.rank[par_b] += self.rank[par_a]
                self.parent[par_a] = par_b
                output = self.rank[par_b]
        else:
            output = self.rank[par_a]

        output_file.write(f"{output} \n")

input_file = open("input1_2.txt", 'r')
output_file = open("output1_2.txt", 'w')
N, K = map(int, input_file.readline().split())
obj = disjointSet(N)
for _ in range(K):
    a, b = map(int, input_file.readline().split())
    obj.union(a,b)