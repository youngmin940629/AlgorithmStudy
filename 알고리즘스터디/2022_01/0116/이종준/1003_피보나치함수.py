def fibo(n):
    for i in range(2, n + 1):
        zero_dp.append(zero_dp[i - 1] + zero_dp[i - 2])
        one_dp.append(one_dp[i - 1] + one_dp[i - 2])

T = int(input())
for tc in range(T):
    zero_dp = [1, 0]
    one_dp = [0, 1]
    N = int(input())
    fibo(N)
    print(zero_dp[N], end=' ')
    print(one_dp[N])