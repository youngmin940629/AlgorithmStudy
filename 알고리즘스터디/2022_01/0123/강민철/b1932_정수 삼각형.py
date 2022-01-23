import sys;sys.stdin = open('1932.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]
dp[0][0] = arr[0][0]
for i in range(1, N):
    dp[i][0] = dp[i-1][0] + arr[i][0]
    dp[i][i] = dp[i-1][i-1] + arr[i][i]
    for j in range(1, i):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + arr[i][j]

print(max(dp[N-1]))