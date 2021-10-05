from collections import deque
def is_safe(x, y):
    return 0 <= x < N and 0 <= y < M

def bfs():
    global area
    while q:
        x, y = q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if is_safe(nx, ny) and not visited[ny][nx] and square[ny][nx] == 0:
                visited[ny][nx] = 1
                square[ny][nx] = -1
                area += 1
                q.append((nx, ny))

M, N, K = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(K)]
square = [[0] * N for _ in range(M)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for idx in range(K):
    for x in range(data[idx][0], data[idx][2]):
        for y in range(data[idx][1], data[idx][3]):
            square[y][x] = 1
visited = [[0] * N for _ in range(M)]
result = []
result_cnt = 0
q = deque()
for x in range(N):
    for y in range(M):
        if square[y][x] == 0:
            visited[y][x] = 1
            square[y][x] = -1
            q.append((x,y))
            area = 1
            bfs()
            result_cnt += 1
            result.append(area)
result.sort()
print(result_cnt)
print(' '.join(map(str, result)))