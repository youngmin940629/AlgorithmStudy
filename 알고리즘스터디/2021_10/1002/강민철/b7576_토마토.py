import sys;sys.stdin = open('7576.txt')

# BFS
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

start = list()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            start.append([i, j])

que = [0] * (N*M)
F = R = -1

for crd in start:
    F += 1
    que[F] = crd

target = 1
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
while F > R:
    R += 1
    i, j = que[R][0], que[R][1]
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if 0 <= ni < N and 0 <= nj < M and not arr[ni][nj]:
            F += 1
            que[F] = [ni, nj]
            arr[ni][nj] = arr[i][j] + 1
            if arr[ni][nj] > target:
                target = arr[ni][nj]

for i in range(N):
    for j in range(M):
        if not arr[i][j]:
            target = 0
            break
    if not target:
        break

print(target-1)
