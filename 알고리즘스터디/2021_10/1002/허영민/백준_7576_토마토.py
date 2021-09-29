from collections import deque

def bfs():
    while q:
        x, y = q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < M and 0 <= ny < N and visited[ny][nx] == 0 and box[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] + 1
                q.append((nx, ny))


M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q = deque()
for x in range(M):
    for y in range(N):
        if box[y][x] == -1:
            visited[y][x] = -1
for x in range(M):
    for y in range(N):
        if box[y][x] == 1 and not visited[y][x]:
            visited[y][x] = 1
            q.append((x, y))
bfs()
result = 0
break_point = 0
for x in range(M):
    for y in range(N):
        if result < visited[y][x]:
            result = visited[y][x]
        if visited[y][x] == 0:
            result = 0
            break_point = 1
            break
    if break_point == 1:
        break
if result == 0:
    print(-1)
else:
    print(result - 1)