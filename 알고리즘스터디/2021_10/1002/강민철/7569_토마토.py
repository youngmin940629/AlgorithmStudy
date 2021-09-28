from collections import deque

M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for i in range(N)] for j in range(H)]

dq = deque()

for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j] == 1:
                dq.append((h, i, j))

dh = (0, 0, 0, 0, 1, -1)
di = (0, 1, 0, -1, 0, 0)
dj = (1, 0, -1, 0, 0, 0)
while dq:
    loc = dq.popleft()
    h, i, j = loc[0], loc[1], loc[2]
    for d in range(6):
        nh = h + dh[d]
        ni = i + di[d]
        nj = j + dj[d]
        if 0 <= nh < H and 0 <= ni < N and 0 <= nj < M and not arr[nh][ni][nj]:
            arr[nh][ni][nj] = arr[h][i][j] + 1
            dq.append((nh, ni, nj))

day = 1
for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j] > day:
                day = arr[h][i][j]
            elif not arr[h][i][j]:
                day = 0
                break
        if not day:
            break
    if not day:
        break

print(day-1)