def solve(N):
    memo = [[0] * 10 for _ in range(101)]
    memo[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    memo[2] = [1, 1, 2, 2, 2, 2, 2, 2, 2, 1]
    if N <= 2:
        return sum(memo[N])
    for i in range(3, N+1):
        memo[i][0] = memo[i-1][1]
        memo[i][9] = memo[i-1][8]
        for j in range(1, 9):
            memo[i][j] = memo[i-1][j-1] + memo[i-1][j+1]
    return sum(memo[N]) % 1000000000

print(solve(int(input())))