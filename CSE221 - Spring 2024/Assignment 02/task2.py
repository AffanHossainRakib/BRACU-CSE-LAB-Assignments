# Helper Functions
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

def mergeSort(arr, lo, hi) -> list: # Time Complexity O(nlogn)
    if lo == hi:
        return [arr[lo]]

    mid = (lo+hi)//2

    left_arr = mergeSort(arr, lo, mid)
    right_arr = mergeSort(arr, mid+1, hi)

    return merge(len(left_arr), left_arr, len(right_arr), right_arr) # Time Complexity O(n)

def array_writer(arr): # Time Complexity O(n)
    for i in arr:
        output_file.write(f"{i} ")
    output_file.write("\n")

# Main Task 02 starts here
input_file = open("input2.txt", 'r')
output_file = open("output2.txt", 'w')

def task2_1(): # Task 02 Part 01 -  Time Complexity O(nlogn)
    n1 = int(input_file.readline())
    arr1 = list(map(int, input_file.readline().split()))
    n2 = int(input_file.readline())
    arr2 = list(map(int, input_file.readline().split()))

    final_arr = arr1 + arr2

    result = mergeSort(final_arr, 0, len(final_arr)-1)
    array_writer(result)

def task2_2(): # Task 02 Part 02 -  Time Complexity O(n)
    n1 = int(input_file.readline())
    arr1 = list(map(int, input_file.readline().split()))
    n2 = int(input_file.readline())
    arr2 = list(map(int, input_file.readline().split()))

    result = merge(n1, arr1, n2, arr2) # Time Complexity O(n)
    array_writer(result) # Time Complexity O(n)

task2_1() # Time Complexity O(nlog(n))
task2_2() # Time Complexity O(n)

input_file.close()
output_file.close()