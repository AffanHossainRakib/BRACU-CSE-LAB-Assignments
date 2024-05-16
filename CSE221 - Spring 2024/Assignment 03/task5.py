def quickSort(arr, lo, hi):
    if lo < hi:
        p = partition(arr, lo, hi)
        quickSort(arr, lo, p-1)
        quickSort(arr, p+1, hi)


def partition(arr, lo, hi):
    mid = (lo+hi)//2
    arr[lo], arr[mid] = arr[mid], arr[lo]
    
    pivot = arr[lo]
    i = lo

    for j in range(i+1, hi+1):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i], arr[lo] = arr[lo], arr[i]
    return i


def array_writer(arr): # Time Complexity O(n)
    for i in arr:
        output_file.write(f"{i} ")
    output_file.write("\n")


input_file = open("input5.txt", "r")
output_file = open("output5.txt", "w")

def task5():
    n = int(input_file.readline())
    arr = list(map(int, input_file.readline().split()))
    quickSort(arr, 0, n-1)
    array_writer(arr)

task5()

input_file.close()
output_file.close()
