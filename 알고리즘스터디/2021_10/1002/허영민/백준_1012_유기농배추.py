from collections import deque
def bfs():
    while q:
        x, y = q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx] and farm[ny][nx] == 1:
                q.append((nx,ny))
                visited[ny][nx] = 1

for T in range(int(input())):
    M, N, K = map(int, input().split())
    farm = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    result = 0
    q = deque()
    for _ in range(K):
        x, y = map(int, input().split())
        farm[y][x] = 1
    for x in range(M):
        for y in range(N):
            if not visited[y][x] and farm[y][x] == 1:
                visited[y][x] = 1
                q.append((x,y))
                bfs()
                result += 1
    print(result)