def minmumCoins(target, coins):
    values = [float("inf") for i in range(target+1)]
    values[0] = 0

    for i in range(1, target+1):
        for j in coins:
            if i - j >= 0:
                values[i] = min(values[i], 1+values[i-j])

    return values[target] if values[target] != float("inf") else -1 

input_file = open("input4_1.txt", 'r')
output_file = open("output4_1.txt", 'w')
n, x = map(int, input_file.readline().split())
coins = list(map(int, input_file.readline().split()))
output_file.write(str(minmumCoins(x, coins)))