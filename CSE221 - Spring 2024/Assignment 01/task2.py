def optimizedBubbleSort(arr):
    for i in range(len(arr) - 1):
        flag = True
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = False
        if flag:
            break

def task2():
    input_file = open("input2.txt", 'r')
    output_file = open("output2.txt", 'w')

    TC = int(input_file.readline())

    for i in range(TC):
        n = int(input_file.readline())
        arr = list(map(int, input_file.readline().split()))
        optimizedBubbleSort(arr)

        for j in range(n):
            if j < n - 1:
                output_file.write(str(arr[j]) + " ")
            else:
                output_file.write(str(arr[j]))
        
        if i < TC:
            output_file.write("\n")
    
    input_file.close()
    output_file.close()

task2()