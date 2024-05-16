class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


input_file = open("input1b_1.txt", 'r')
output_file = open("output1b_1.txt", 'w')

N, M = map(int, input_file.readline().split())

adjList = [None for i in range(N+1)]

for _ in range(M):  
    u, v, w = map(int, input_file.readline().split())

    node = Node((v,w))

    if adjList[u] is None:
        adjList[u] = [node, node] # head, tail
    else:
        adjList[u][1].next = node
        adjList[u][1] = node


for i in range(N+1):
    output_file.write(f"{i} : ")
    if adjList[i] is not None:
        tail = adjList[i][0]
        while tail is not None:
            output_file.write(f"{tail.value} ")
            tail = tail.next
    output_file.write("\n")

input_file.close()
output_file.close()