def modifiedSelectionSort(n, arr1, arr2):
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n, 1):
            if arr2[j] > arr2[min_idx]:
                min_idx = j
            elif arr2[j] == arr2[min_idx]:
                if arr1[j] < arr1[min_idx]:
                    min_idx = j
        
        if min_idx != i:
            arr1[i], arr1[min_idx] = arr1[min_idx], arr1[i]
            arr2[i], arr2[min_idx] = arr2[min_idx], arr2[i]


def task3():
    input_file = open("input3.txt", 'r')
    output_file = open("output3.txt", 'w')

    TC = int(input_file.readline())

    for i in range(TC):
        output_file.write(f"Output: {i + 1}\n")
        n = int(input_file.readline())
        id = list(map(int, input_file.readline().split()))
        marks = list(map(int, input_file.readline().split()))

        modifiedSelectionSort(n, id, marks)

        for i in range(n):
             output_file.write(f"ID: {id[i]} Mark: {marks[i]}\n")
            
        
    input_file.close()
    output_file.close()

task3()

