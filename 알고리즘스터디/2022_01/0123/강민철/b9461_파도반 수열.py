dp = [0] + [1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + ([0] * 90)

def solve(n):
    if dp[n]:
        return dp[n]
    dp[n] = solve(n-1) + solve(n-5)
    return dp[n]

T = int(input())

for _ in range(T):
    N = int(input())
    print(solve(N))