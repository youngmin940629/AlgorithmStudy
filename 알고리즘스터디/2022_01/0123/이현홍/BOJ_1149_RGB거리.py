N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]


for i in range(1, N):
    for j in range(3):
        prices = []
        for k in range(3):
            if j == k: continue
            prices.append(arr[i][j] + arr[i-1][k])
        arr[i][j] = min(prices)

print(min(arr[-1]))