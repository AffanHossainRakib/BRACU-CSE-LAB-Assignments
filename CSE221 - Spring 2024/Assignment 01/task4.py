def customSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            name_1, name_2 = arr[j][0], arr[j+1][0]
            time_1 = int(arr[j][1][0:2]) * 60 + int(arr[j][1][3::])
            time_2 = int(arr[j+1][1][0:2]) * 60 + int(arr[j+1][1][3::])

            if name_1 == name_2 and time_1 < time_2:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                k = 0
                flag = True
                while k < len(name_1) and k < len(name_2):
                    if name_1[k] == name_2[k]:
                        k += 1
                    else:
                        flag = False
                        if ord(name_1[k]) > ord(name_2[k]):
                            arr[j], arr[j+1] = arr[j+1], arr[j]
                        break
                if flag and len(name_1) > len(name_2):
                        arr[j], arr[j+1] = arr[j+1], arr[j]
                    
                    
def task4():
    input_file = open("input4.txt", 'r')
    output_file = open("output4.txt", 'w')

    n = int(input_file.readline())
    all_trains = []

    for _ in range(n):
        train =  tuple(input_file.readline().split())
        all_trains.append((train[0], train[6], train[4]))
    
    customSort(all_trains)
    for i in all_trains:
        output_file.write(f"{i[0]} will departure for {i[2]} at {i[1]}\n")

    input_file.close()
    output_file.close()

task4()
