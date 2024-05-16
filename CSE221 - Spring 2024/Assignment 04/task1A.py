input_file = open("input1a_1.txt", 'r')
output_file = open("output1a_1.txt", 'w')

N, M = map(int, input_file.readline().split())

adjMat = [[0 for i in range(N+1)] for i in range(N+1)]

for _ in range(M):
    u, v, w = map(int, input_file.readline().split())
    adjMat[u][v] = w
    
for row in adjMat:
    for item in row:    
        output_file.write(str(item)+" ")
    output_file.write("\n")

input_file.close()
output_file.close()