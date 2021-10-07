from collections import deque


M, N = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(M)]
check = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cheese_cnt = []
time = 0
def melting_cheese():
    global time
    visited = [[0] * N for _ in range(M)]
    cnt = 0
    while check:
        x, y = check.popleft()
        visited[y][x] = 1
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < N and 0 <= ny < M and not visited[ny][nx]:
                if cheese[ny][nx] == 0:
                    visited[ny][nx] = 1
                    check.append((nx,ny))
                elif cheese[ny][nx] == 1:
                    visited[ny][nx] = 1
                    cheese[ny][nx] = 0
                    cnt += 1
    cheese_cnt.append(cnt)
    time += 1
    return cnt
while True:
    check.append((0, 0))
    if melting_cheese() == 0:
        break

print(time - 1)
print(cheese_cnt[-2])