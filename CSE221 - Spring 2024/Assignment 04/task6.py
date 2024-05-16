class Graph():
    def __init__(self, R, H):
        self.row = R
        self.col = H
        self.graph = [[0 for i in range(H)] for j in range(R)]

    def addEdge(self, i, j, v):
        self.graph[i][j] = v
    
    def collected(self):
        self.visited = [[0 for i in range(H)] for j in range(R)]
        self.COUNTER = []

        for i in range(self.row):
            for j in range(self.col):
                if not self.visited[i][j] and self.graph[i][j] != "#":
                    self.bfs(i,j)
        
        output_file.write(str(max(self.COUNTER)))

    def bfs(self, i, j):
        self.visited[i][j] = 1
        q = [(i,j)]
        count = 0
        while q:
            a, b = q.pop(0)
            if self.graph[a][b] == "D":
                count += 1

            if self.valid(a+1, b): 
                q.append((a+1, b))
                self.visited[a+1][b] = 1

            if self.valid(a-1, b): 
                q.append((a-1, b))
                self.visited[a-1][b] = 1

            if self.valid(a, b+1):
                q.append((a, b+1))
                self.visited[a][b+1] = 1
                
            if self.valid(a, b-1): 
                q.append((a, b-1))
                self.visited[a][b-1] = 1

        self.COUNTER.append(count)

    def valid(self, i, j):
        if 0 <= i < self.row and 0 <= j < self.col:
            if not self.visited[i][j] and self.graph[i][j] != "#":
                return True
        return False



input_file = open("input6_7.txt", 'r')
output_file = open("output6_7.txt", 'w')

R, H = map(int, input_file.readline().split())
G = Graph(R, H)
for i in range(R):
    temp = input_file.readline()
    for j in range(H):
        G.addEdge(i, j, temp[j])
G.collected()
