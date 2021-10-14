from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)

def change_map(x,y,num):
    data[x][y] = num
    visited[x][y] = 1
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and data[nx][ny] == 1:
            visited[nx][ny] = 1
            data[nx][ny] = num
            change_map(nx,ny,num)

def bridge(num):
    global result
    q = deque()
    distance = [[-1] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if data[x][y] == num:
                q.append((x,y))
                distance[x][y] = 0
    while q:
        x, y = q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < N and 0 <= ny < N:
                if data[nx][ny] == 0 and distance[nx][ny] == -1:
                    distance[nx][ny] = distance[x][y] + 1
                    q.append((nx,ny))
                elif data[nx][ny] > 0 and data[nx][ny] != num:
                    result = min(result, distance[x][y])
                    return
N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
num = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = N * N
for x in range(N):
    for y in range(N):
        if data[x][y] == 1 and not visited[x][y]:
            num += 1
            change_map(x,y,num)
for land in range(1, num+1):
    bridge(land)
print(result)