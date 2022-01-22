N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(i + 1):
        if j == 0:
            data[i][j] += data[i-1][j]
        elif j == i:
            data[i][j] += data[i-1][i-1]
        else:
            data[i][j] += max(data[i-1][j-1], data[i-1][j])

print(max(data[-1]))