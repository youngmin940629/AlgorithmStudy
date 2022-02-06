N = int(input())
data = []
for _ in range(N):
    stair = int(input())
    data.append(stair)
dp = [0] * N
dp[0] = data[0]
if N > 1:
    dp[1] = max(data[1] + data[0], data[1])
if N > 2:
    dp[2] = max(data[2] + data[1], data[2] + data[0])
for i in range(3, N):
    dp[i] = max(dp[i-3] + data[i-1] + data[i], dp[i-2] + data[i])

print(dp[N-1])