# Helper Functions
def merge(n1, arr1, n2, arr2) -> list: # Time Complexity O(n)
    final_arr = [None] * (n1 + n2) 
    i, j, k = 0, 0, 0
    while i < n1 and j < n2:
        if arr1[i][1] < arr2[j][1]:
            final_arr[k] = arr1[i]
            i += 1
        else:
            final_arr[k] = arr2[j]
            j += 1
        k += 1

    while i < n1:
        final_arr[k] = arr1[i]
        i += 1
        k += 1

    while j < n2:
        final_arr[k] = arr2[j]
        j += 1
        k += 1

    return final_arr

def mergeSort(arr, lo, hi) -> list: # Time Complexity O(nlogn)
    if lo == hi:
        return [arr[lo]]

    mid = (lo+hi)//2

    left_arr = mergeSort(arr, lo, mid)
    right_arr = mergeSort(arr, mid+1, hi)

    n1 = len(left_arr)
    n2 = len(right_arr)

    return merge(n1, left_arr, n2, right_arr) # Time Complexity O(n)


# Main Task 03 starts here
input_file = open("input3.txt","r")
output_file = open("output3.txt","w")

def task3():
    n = int(input_file.readline())
    all_tasks = []

    for _ in range(n):
        start, end = map(int, input_file.readline().split())
        all_tasks.append((start,end))
    
    sorted_tasks = mergeSort(all_tasks, 0, n-1) # Time Complexity O(nlogn)

    counter, end, can_do = 0, 0, []
    for i in sorted_tasks:
        if i[0] >= end:
            counter += 1
            end = i[1]
            can_do.append(i)
    
    output_file.write(f"{counter}\n")
    for i in can_do:
        output_file.write(f"{i[0]} {i[1]}\n")


task3()

input_file.close()
output_file.close()