def divide(arr, lo, hi) -> tuple:
    if lo >= hi:
        return float("-inf"), arr[lo]
    
    if hi - lo == 1:
        i, j = arr[lo], arr[hi]
        res = i + j**2
        if abs(i) < abs(j):
            i = j
        return res, i

    mid = (lo+hi)//2
    left = divide(arr, lo, mid)
    right = divide(arr, mid+1, hi)

    i, j = left[1], right[1]
    res = i + j**2
    
    if abs(i) < abs(j):
        i = j 
    return max(left[0], res, right[0]), i

input_file = open("input4.txt", 'r')
output_file = open("output4.txt", 'w')
def task4():
    n = int(input_file.readline())
    arr = list(map(int, input_file.readline().split()))
    returned_value = divide(arr, 0, n-1)
    output_file.write(str(returned_value[0]))

task4()
input_file.close()
output_file.close()