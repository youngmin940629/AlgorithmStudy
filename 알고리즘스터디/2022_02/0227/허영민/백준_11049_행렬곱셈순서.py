N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))
dp = [[0] * N for _ in range(N)]
for dist in range(1, N):
    for i in range(N-dist):
        j = dist + i
        dp[i][j] = 2 ** 32 - 1
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + matrix[i][0] * matrix[k][1]*matrix[j][1])
print(dp[0][N-1])
