N = int(input())
triangle = [list(map(int, input().split())) for _ in range(N)]

for i in range(N-1):
    for j in range(i+1):
        if j == 0:
            triangle[i+1][0] += triangle[i][0]
        if j == i or triangle[i][j] > triangle[i][j+1]:
            triangle[i+1][j+1] += triangle[i][j]
        else:
            triangle[i+1][j+1] += triangle[i][j+1]

print(max(triangle[-1]))