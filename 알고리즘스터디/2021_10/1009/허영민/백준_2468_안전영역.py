from collections import deque
def is_safe(x, y):
    return 0 <= x < N and 0 <= y < N

def bfs():
    while q:
        x, y = q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if is_safe(nx, ny) and not visited[nx][ny] and tmp_area[nx][ny] != -1:
                visited[nx][ny] = 1
                q.append((nx, ny))


N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
result = [1]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
max_height = 0
min_height = 101
q = deque()
for x in range(N):
    for y in range(N):
        if area[x][y] > max_height:
            max_height = area[x][y]
        if area[x][y] < min_height:
            min_height = area[x][y]
for height in range(min_height, max_height):
    tmp_area = [value[:] for value in area]
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for x in range(N):
        for y in range(N):
            if tmp_area[x][y] <= height:
                tmp_area[x][y] = -1
    for x in range(N):
        for y in range(N):
            if tmp_area[x][y] != -1 and not visited[x][y]:
                cnt += 1
                visited[x][y] = 1
                q.append((x,y))
                bfs()
    result.append(cnt)
print(max(result))