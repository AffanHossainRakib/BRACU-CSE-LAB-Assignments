# Helper Functions
def merge(n1, arr1, n2, arr2) -> list: # Time Complexity O(n)
    final_arr = [None] * (n1 + n2) 
    i, j, m = 0, 0, 0
    while i < n1 and j < n2:
        if arr1[i][1] < arr2[j][1]:
            final_arr[m] = arr1[i]
            i += 1
        else:
            final_arr[m] = arr2[j]
            j += 1
        m += 1

    while i < n1:
        final_arr[m] = arr1[i]
        i += 1
        m += 1

    while j < n2:
        final_arr[m] = arr2[j]
        j += 1
        m += 1

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


# Main Task 04 starts here
input_file = open("input4.txt","r")
output_file = open("output4.txt","w")

def task4():
    n, m = map(int, input_file.readline().split())
    all_tasks = []

    for _ in range(n):
        start, end = map(int, input_file.readline().split())
        all_tasks.append((start,end))
    
    sorted_tasks = mergeSort(all_tasks, 0, n-1) # Time Complexity O(nlogn)

    dict = {}
    for i in range(m):
        dict[f"Person {i+1}"] = {"counter": 0, "end": 0}

    counter = 0
    for i in sorted_tasks:   
        max_key, max_end = None, None
        for j in dict: 
            if i[0] >= dict[j]["end"]:
                if max_end == None:
                    max_key = j
                    max_end = dict[max_key]["end"]
                elif dict[j]["end"] > dict[max_key]["end"]:
                    max_key = j
                    max_end = dict[max_key]["end"]

        if max_key != None:
            dict[max_key]["end"] = i[1]
            counter += 1
        
    output_file.write(str(counter))
task4()