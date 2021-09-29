from collections import deque

M, N, H = map(int, input().split())
box = [[] for _ in range(H)]
for height in range(H):
    box[height] = [list(map(int, input().split())) for _ in range(N)]
visited = [[[0] * M for _ in range(N)] for __ in range(H)]
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
result = 0
que = deque()


def bfs():
    while que:
        x, y, z = que.popleft()
        for dir in range(6):
            next_x, next_y, next_z = x+dx[dir], y+dy[dir], z+dz[dir]
            if is_safe(next_x, next_y, next_z):
                if box[next_z][next_y][next_x] == 0 and visited[next_z][next_y][next_x] == 0:
                    visited[next_z][next_y][next_x] = visited[z][y][x] + 1
                    box[next_z][next_y][next_x] = 1
                    que.append([next_x, next_y, next_z])


def is_safe(x,y,z):
    return 0 <= x < M and 0 <= y < N and 0 <= z < H


for z in range(H):
    for y in range(N):
        for x in range(M):
            if box[z][y][x] == 1 and visited[z][y][x] == 0:
                visited[z][y][x] = 1
                que.append([x,y,z])
bfs()
for z in range(H):
    for y in range(N):
        for x in range(M):
            if visited[z][y][x] > result:
                result = visited[z][y][x] - 1

for z in range(H):
    for y in range(N):
        for x in range(M):
            if box[z][y][x] == 0:
                result = -1

print(result)