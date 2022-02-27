import sys

for _ in range(int(sys.stdin.readline())):
    T = int(sys.stdin.readline())
    files = list(map(int, sys.stdin.readline().split()))
    dp = [[0] * (T+1) for _ in range(T+1)]
    s = [0] * (T+1)
    for i in range(1, T+1):
        s[i] = s[i-1] + files[i-1]
    
    for i in range(2, T+1):
        for j in range(1, T+2-i):
            dp[j][i+j-1] = 100000000
            for k in range(i-1):
                tmp = dp[j][j+k] + dp[j+k+1][j+i-1]
                dp[j][j+i-1] = min(dp[j][j+i-1], tmp)
            dp[j][j+i-1] += s[j+i-1] - s[j-1]
    print(dp[1][T])