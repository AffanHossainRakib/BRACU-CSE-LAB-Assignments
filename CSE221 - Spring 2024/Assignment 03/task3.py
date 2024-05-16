COUNTER = 0 # GLOBAL COUNTER

def divide(arr, lo, hi):
    if lo >= hi:
        return [arr[lo]]
    
    mid = (lo+hi)//2
    left = divide(arr, lo, mid)
    right = divide(arr, mid+1, hi)
    return merge(left,right)

def merge(arr1, arr2):
    n1, n2 = len(arr1), len(arr2)
    res = [None]*(n1+n2)

    i = j = k = 0
    while i < n1 and j < n2:
        if arr1[i] <= arr2[j]:
            res[k] = arr1[i]
            i += 1

        else:
            res[k] = arr2[j]
            j += 1
            global COUNTER 
            COUNTER +=  n1 - i    
        k += 1
    
    while i < n1:
        res[k] = arr1[i]
        i += 1
        k += 1
    
    while j < n2:
        res[k] = arr2[j]
        j += 1
        k += 1
        
    return res


input_file = open("input3.txt", 'r')
output_file = open("output3.txt", 'w')
def task3():
    n = int(input_file.readline())
    arr = list(map(int, input_file.readline().split()))
    divide(arr, 0, n-1)
    output_file.write(str(COUNTER))

task3()
input_file.close()
output_file.close()