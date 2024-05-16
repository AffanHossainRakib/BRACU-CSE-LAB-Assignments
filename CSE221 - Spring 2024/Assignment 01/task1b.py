def task1b():
    input_file = open("input1b.txt", 'r')
    output_file = open("output1b.txt", 'w')

    TC = int(input_file.readline())

    for _ in range(TC):
        arr = input_file.readline().split()
        
        if arr[2] == "+":
            output_file.write(f"The result of {arr[1]} + {arr[3]} is {int(arr[1]) + int(arr[3])}\n")
        elif arr[2] == "-":
            output_file.write(f"The result of {arr[1]} - {arr[3]} is {int(arr[1]) - int(arr[3])}\n")
        elif arr[2] == "*":
            output_file.write(f"The result of {arr[1]} * {arr[3]} is {int(arr[1]) * int(arr[3])}\n")
        elif arr[2] == "/":
            output_file.write(f"The result of {arr[1]} / {arr[3]} is {int(arr[1]) / int(arr[3])}\n")
    
    input_file.close()
    output_file.close()
    
task1b()