from collections import deque
def bfs():
    while q:
        x, y = q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if grid[nx][ny] == grid[x][y]:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
N = int(input())
grid = [list(input()) for _ in range(N)]
result = [0] * 2
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[0] * N for _ in range(N)]
q = deque()
cnt = 0
for x in range(N):
    for y in range(N):
        if not visited[x][y]:
            q.append((x,y))
            bfs()
            cnt += 1
result[0] = cnt
cnt = 0
for x in range(N):
    for y in range(N):
        visited[x][y] = 0
        if grid[x][y] == 'R':
            grid[x][y] = 'G'
for x in range(N):
    for y in range(N):
        if not visited[x][y]:
            q.append((x,y))
            bfs()
            cnt += 1
result[1] = cnt
print(result[0], result[1])