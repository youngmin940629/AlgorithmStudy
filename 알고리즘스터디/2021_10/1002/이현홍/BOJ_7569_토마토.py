M, N, H = map(int, input().split())
arr = [[[0] for _ in range(N)] for _ in range(H)]
Q = [0] * M * N * H
front = -1
rear = -1

for h in range(H):
    for n in range(N):
        arr[h][n] = list(map(int, input().split()))



dr = [0, 0, 0, 0, 1, -1]
dc = [0, 0, 1, -1, 0, 0]
dh = [1, -1, 0, 0, 0, 0]
def BFS(h, r, c, n):
    for k in range(6):
        nr = r + dr[k]
        nc = c + dc[k]
        nh = h + dh[k]
        if 0 <= nr < N and 0 <= nc < M and 0 <= nh < H:
            if arr[nh][nr][nc] == 0:
                arr[nh][nr][nc] = n + 1
                global rear, answer
                rear += 1
                Q[rear] = (nh, nr, nc, n + 1)
                if n+1 > answer:
                    answer = n+1

for h in range(H):
    for r in range(N):
        for c in range(M):
            if arr[h][r][c] == 1:
                rear += 1
                Q[rear] = (h, r, c, 0)
answer = 0

while front != rear:
    front += 1
    h = Q[front][0]
    r = Q[front][1]
    c = Q[front][2]
    n = Q[front][3]
    BFS(h, r, c, n)

for h in range(H):
    for r in range(N):
        flag = 0
        for c in range(M):
            if arr[h][r][c] == 0:
                flag = 1
                break
        if flag: break
    if flag:
        answer = -1
        break
print(answer)

