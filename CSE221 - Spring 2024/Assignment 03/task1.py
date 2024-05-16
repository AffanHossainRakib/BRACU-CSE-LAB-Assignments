def mergeSort(arr, lo, hi) -> list: # Time Complexity O(nlogn)
    if lo == hi:
        return [arr[lo]]

    mid = (lo+hi)//2

    left_arr = mergeSort(arr, lo, mid)
    right_arr = mergeSort(arr, mid+1, hi)

    return merge(len(left_arr), left_arr, len(right_arr), right_arr) # Time Complexity O(n)

def merge(n1, arr1, n2, arr2) -> list: # Time Complexity O(n)
    final_arr = [None] * (n1 + n2) 
    i, j, k = 0, 0, 0
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
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

def array_writer(arr): # Time Complexity O(n)
    for i in arr:
        output_file.write(f"{i} ")
    output_file.write("\n")

input_file = open("input1.txt", "r")
output_file = open("output1.txt", "w")

def task1():
    n = int(input_file.readline())
    arr = list(map(int, input_file.readline().split()))
    sorted_arr = mergeSort(arr, 0, n-1)
    array_writer(sorted_arr)

task1()

input_file.close()
output_file.close()