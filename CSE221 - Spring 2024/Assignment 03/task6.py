def find_kth(arr, lo, hi, k):
    if lo > hi:
        return 
    
    pivot = arr[lo]
    i = lo
    for j in range(lo+1, hi+1):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[lo], arr[i] = arr[i], arr[lo]
    
    if i == k:
        return arr[i]
    elif i < k:
        return find_kth(arr, i+1, hi, k)
    return find_kth(arr, lo, i-1, k)

input_file = open("input6.txt", 'r')
output_file = open("output6.txt", 'w')

def task6():
    n = int(input_file.readline())
    arr = list(map(int, input_file.readline().split()))
    q = int(input_file.readline())
    for i in range(q):
        k = int(input_file.readline())
        res = find_kth(arr, 0, n-1, k-1)
        output_file.write(str(res)+"\n")
task6()

input_file.close()
output_file.close()