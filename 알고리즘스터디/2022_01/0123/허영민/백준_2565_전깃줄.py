N = int(input())
wire = []
for _ in range(N):
    wire.append(list(map(int, input().split())))
wire.sort()
dp = [0] * N
for i in range(N):
    for j in range(i):
        if wire[i][1] > wire[j][1] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(N-max(dp))