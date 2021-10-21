from collections import deque

def bfs():
    visited = [[0] * W for _ in range(H)]
    result = 0
    while q:
        x, y = q.popleft()
        for dir in range(8):
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < W and 0 <= ny < H:
                if arr[ny][nx] != 0:
                    arr[ny][nx] -= 1
                    if arr[ny][nx] == 0:
                        q.append((nx,ny))
                        visited[ny][nx] = visited[y][x] + 1
                        result = max(result, visited[ny][nx])
    return result

H, W = map(int,input().split())
arr = [list(input()) for _ in range(H)]
dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
q = deque()
result = 0
for x in range(W):
    for y in range(H):
        if arr[y][x] == '.':
            q.append((x, y))
            arr[y][x] = 0
        else:
            arr[y][x] = int(arr[y][x])
print(bfs())