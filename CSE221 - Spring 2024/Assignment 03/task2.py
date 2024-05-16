def find_peak(arr, lo, hi):
    if lo == hi:
        return arr[lo]
    
    mid = (lo+hi)//2
    left = find_peak(arr, lo, mid)
    right = find_peak(arr, mid+1, hi)

    return max(left, right)

input_file = open("input2.txt", "r")
output_file = open("output2.txt", "w")

def task2():
    n = int(input_file.readline())
    arr = list(map(int, input_file.readline().split()))
    output_file.write(str(find_peak(arr, 0, n-1)))
    
task2()

input_file.close()
output_file.close()