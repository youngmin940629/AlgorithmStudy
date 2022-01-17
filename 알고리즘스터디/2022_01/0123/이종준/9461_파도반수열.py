def wave(n):
    for i in range(5, n + 1):
        dp.append(dp[i-1] + dp[i-5])

T = int(input())
for _ in range(T):
    dp = [1, 1, 1, 2, 2]
    N = int(input())
    wave(N)
    print(dp[N-1])