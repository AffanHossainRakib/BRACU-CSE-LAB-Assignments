def steps(n, memo):
    if memo[n] != -1:
        return memo[n]
    memo[n] = steps(n-1, memo) + steps(n-2, memo)
    return memo[n]


input_file = open("input3_4.txt", 'r')
output_file = open("output3_4.txt", 'w')
n = int(input_file.readline())
memo = [-1]*(n+1)
memo[1] = 1
memo[2] = 2

output_file.write(str(steps(n, memo)))