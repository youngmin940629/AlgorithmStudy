from collections import deque

N, M = map(int, input().split())
data = [list(input()) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q = deque()
q.append((0,0,0))
def bfs():
    visited = [[[0] * M for _ in range(N)] for _ in range(2)]
    visited[0][0][0] = 1
    while q:
        x,y,work = q.popleft()
        if x == N-1 and y == M - 1:
            return visited[work][x][y]
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < N and 0 <= ny < M:
                if data[nx][ny] == '0' and not visited[work][nx][ny]:
                    visited[work][nx][ny] = visited[work][x][y] + 1
                    q.append((nx,ny,work))
                elif data[nx][ny] == '1' and work == 0:
                    visited[1][nx][ny] = visited[0][x][y] + 1
                    q.append((nx,ny,1))
    return -1
print(bfs())