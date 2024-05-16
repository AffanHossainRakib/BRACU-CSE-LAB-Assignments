input_file = open("input1.txt", 'r')
output_file = open("output1.txt", 'w')

# Task 01 Part 01 - Time Complexity O(N^2)
def task1_1():
    n, target = map(int, input_file.readline().split())
    arr = list(map(int, input_file.readline().split()))

    flag = True

    for j in range(n):
        for k in range(n):
            if j != k:
                if target - arr[j] - arr[k] == 0:
                    output_file.write(f"{j+1} {k+1}\n")
                    flag = False
                    break

        if not flag:
            break
            
    if flag:
        output_file.write(f"IMPOSSIBLE\n")
    

            
# Task 01 Part 02 -  Time Complexity O(N)
def task1_2(): 
    n, target = map(int, input_file.readline().split())
    arr = list(map(int, input_file.readline().split()))

    flag = True
    i, j  = 0, n-1
    while i < j:
        if arr[i] + arr[j] == target:
            output_file.write(f"{i+1} {j+1}\n")
            flag = False
            break
        elif arr[i] + arr[j] < target:
            i += 1
        else:
            j -= 1
                
            
    if flag:
        output_file.write(f"IMPOSSIBLE\n")


task1_1() # Time Complexity O(N^2)
task1_2() # Time Complexity O(N)
    
input_file.close()
output_file.close()