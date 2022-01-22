N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
for i in range(1, N):
    data[i][0] += min(data[i-1][1], data[i-1][2])
    data[i][1] += min(data[i-1][0], data[i-1][2])
    data[i][2] += min(data[i-1][1], data[i-1][0])

print(min(data[N-1]))