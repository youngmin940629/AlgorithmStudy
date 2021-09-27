M, N = map(int, input().split())
arr = [0] * N
for n in range(N):
    arr[n] = list(map(int, input().split()))


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def BFS(r, c, n):
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < M:
            if arr[nr][nc] == 0:
                arr[nr][nc] = n + 1
                global rear, answer
                rear += 1
                Q[rear] = (nr, nc, n + 1)
                if answer < n+1:
                    answer = n+1

Q = [0] * M * N
front = -1
rear = -1

for r in range(N):
    for c in range(M):
        if arr[r][c] == 1:
            rear += 1
            Q[rear] = (r, c, 1)
answer = 0
while front != rear:
    front += 1
    r = Q[front][0]
    c = Q[front][1]
    n = Q[front][2]
    BFS(r, c, n)
if answer: answer -= 1

for r in range(N):
    flag = 0
    for c in range(M):
        if arr[r][c] == 0:
            flag = 1
            break
    if flag:
        answer = -1
        break

print(answer)






