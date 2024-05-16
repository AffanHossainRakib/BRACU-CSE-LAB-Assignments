def task1a():
    input_file = open("input1a.txt", 'r')
    output_file = open("output1a.txt", 'w')

    TC = int(input_file.readline())

    for _ in range(TC):
        n = int(input_file.readline())
        if (n & 1) == 0:
            output_file.write(f"{n} is an Even number.\n")
        else:
            output_file.write(f"{n} is an Odd number.\n")

    input_file.close()
    output_file.close()
            
task1a()