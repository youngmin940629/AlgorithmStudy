# 시간초과 => 델타함수를 조건문으로 해야 안난다함 노가다라 패스.. 시간만 뻇은문제

from collections import deque
def bfs(a,b):
    visited = [[0] * N for _ in range(M)]
    max_val = 0
    q = deque([(a,b)])
    visited[b][a] = 1
    while q:
        x, y = q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < N and 0 <= ny < M and not visited[ny][nx]:
                if data[ny][nx] == 'L':
                    visited[ny][nx] = visited[y][x] + 1
                    if max_val < visited[ny][nx]:
                        max_val = visited[ny][nx]
                    q.append((nx, ny))
    return max_val - 1


M, N = map(int, input().split())
data = [list(input()) for _ in range(M)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = 0
for x in range(N):
    for y in range(M):
        if data[y][x] == 'L':
            result = max(result, bfs(x,y))
print(result)
